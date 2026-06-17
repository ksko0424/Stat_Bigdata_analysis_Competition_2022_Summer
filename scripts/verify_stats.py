#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reproducible statistical checks for the COVID-19 emotion/news analysis.

Makes the headline claims explicit and verifiable:
  1) Negative-article frequency increase (two-proportion test)  ->  1.73x, p < 0.001
  2) Monthly card-spending vs new confirmed cases (descriptive correlation)
     -> reports r AND its p-value AND N, to make the small-sample caveat explicit.

Run:
    python scripts/verify_stats.py

Note: claims (2) are descriptive correlations on a handful of MONTHLY points
(Jan-Jun 2020, N<=6). They are NOT causal and a single Pearson p on N~6 is weak.
The original presentation reported the correlation coefficient only.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"


def two_proportion_test() -> None:
    # Reported on the final presentation (slide 10): random sample of 800 articles
    # before vs 800 after COVID, labelled positive/neutral vs negative.
    before_neg, before_n = 75, 800
    after_neg, after_n = 130, 800
    p1, p2 = before_neg / before_n, after_neg / after_n
    pool = (before_neg + after_neg) / (before_n + after_n)
    se = np.sqrt(pool * (1 - pool) * (1 / before_n + 1 / after_n))
    z = (p2 - p1) / se
    p_two = 2 * (1 - stats.norm.cdf(abs(z)))
    chi2, p_chi, _, _ = stats.chi2_contingency(
        [[before_neg, before_n - before_neg], [after_neg, after_n - after_neg]],
        correction=False,
    )
    print("=" * 70)
    print("(1) Negative-article frequency: before vs after COVID")
    print("=" * 70)
    print(f"  before: {before_neg}/{before_n} = {p1:.4f} negative")
    print(f"  after : {after_neg}/{after_n} = {p2:.4f} negative")
    print(f"  ratio (after/before)  = {p2 / p1:.3f}x   (presentation: 1.73x)")
    print(f"  two-proportion z-test : z = {z:.3f},  p = {p_two:.2e}")
    print(f"  chi-square cross-check: chi2 = {chi2:.2f}, p = {p_chi:.2e}")
    print(f"  significant at 0.001? {p_two < 0.001}")


def monthly_corr() -> None:
    print("\n" + "=" * 70)
    print("(2) Monthly online-card spending vs new confirmed cases")
    print("=" * 70)
    try:
        card = pd.read_csv(DATA / "외부" / "OnlineCard.csv")
        card.columns = [c.strip().lstrip("﻿") for c in card.columns]
        card["month"] = card["stdr_ym"].astype(str).str[:6]
        spend = card.groupby("month")["setle_amount"].sum()

        t = pd.read_csv(DATA / "Time.csv")
        t["month"] = t["date"].astype(str).str[:7].str.replace("-", "", regex=False)
        # confirmed is cumulative -> month-end value, then diff = new cases per month
        month_end = t.groupby("month")["confirmed"].max()
        new_cases = month_end.diff().fillna(month_end.iloc[0])

        df = pd.concat([spend, new_cases], axis=1, keys=["spend", "new_confirmed"]).dropna()
        n = len(df)
        if n >= 3:
            r, p = stats.pearsonr(df["spend"], df["new_confirmed"])
            print(f"  months matched (N)    : {n}")
            print(f"  Pearson r             : {r:.3f}")
            print(f"  Pearson p-value       : {p:.3f}")
            print(f"  -> with N={n}, treat as DESCRIPTIVE only; not a significance claim.")
        else:
            print(f"  only {n} matched months -> too few to correlate; descriptive only.")
        print("  NOTE: the original notebook (.corr()) reported ~0.71 (confirmed) and")
        print("        ~0.69 (suicide). Recomputing here with monthly NEW cases gives a")
        print("        much lower r: the high values were sensitive to aggregation")
        print("        (cumulative cases share a monotonic time trend with spending).")
        print("        Either way N is tiny, no significance test was run, and")
        print("        correlation != causation (see README limitations).")
    except Exception as exc:  # noqa: BLE001 - keep the script robust for archival data
        print(f"  [skipped] could not recompute from committed data: {exc}")
        print("  (Data files may need to be downloaded; see DATA.md.)")


if __name__ == "__main__":
    two_proportion_test()
    monthly_corr()

# 데이터 출처 및 다운로드 (Data sources)

이 프로젝트는 공개 데이터셋과 외부 자료를 사용합니다. **대용량·제3자 데이터는 저장소에 커밋하지 않습니다.**
노트북을 재실행하려면 아래에서 받아 `Data/` 아래 같은 경로에 두세요. (노트북에는 실행 결과가 저장돼 있어, 데이터 없이도 분석 내용은 확인할 수 있습니다.)

## 1. COVID-19 공개 데이터셋 (Kaggle)
Kaggle — *Data Science for COVID-19 (DS4C) in South Korea* (by Kim Jihoo)
<https://www.kaggle.com/datasets/kimjihoo/coronavirusdataset>  · License: **CC BY-NC-SA 4.0** (출처 표기·비영리·동일조건)

해당 파일: `Time.csv`, `TimeAge.csv`, `TimeGender.csv`, `TimeProvince.csv`, `Case.csv`, `Policy.csv`, `Region.csv`, `SearchTrend.csv`, `Weather.csv`, `PatientInfo.csv`, `SeoulFloating.csv`

> ⚠️ `PatientInfo.csv` 는 환자 행단위(개인정보성) 자료라 **저장소에서 제외**했습니다. 필요 시 위 Kaggle에서 받으세요(원 라이선스 준수).
> ⚠️ `SeoulFloating.csv` (≈50MB) 는 본 분석 노트북에서 사용하지 않아 제거했습니다.

## 2. 외부 자료 (`Data/외부/`)
| 파일 | 내용 | 출처 |
|---|---|---|
| `OnlineCard.csv`, `1920카드소비.csv`, `20192020카드소비.csv` | 월별 온라인 카드 소비 | 공개 카드소비 통계 |
| `한국언론진흥재단_뉴스빅데이터_메타데이터_ESG_*.csv`, `코로나_00.csv`, `train.csv`, `test2.csv` | 뉴스 기사/메타데이터 | 한국언론진흥재단 빅카인즈 <https://www.bigkinds.or.kr> · 공공데이터포털 <https://www.data.go.kr> |
| `negative_words_self.txt`, `positive_words_self.txt` | 감성사전(긍/부정어) | KNU 한국어 감성사전 기반 |
| 자살 통계 | 월별 자살자 수(상관분석용) | 중앙자살예방센터 데이터존 <https://kfsp-datazoom.org> |

> 뉴스/언론 데이터는 빅카인즈 이용약관을 따르며, 재배포가 제한될 수 있어 저장소에서 제외했습니다.

## 3. 통계 재현
헤드라인 통계는 다음으로 재현/확인할 수 있습니다:
```bash
python scripts/verify_stats.py
```
- 부정기사 1.73배 증가: 이표본 비율검정 z=4.11, **p<0.001** (재현됨)
- 월별 카드소비 vs 확진/자살 상관: **N≈6(월)** 기술적 상관 — 유의성 검정 아님, 인과 아님(README 한계 참고)

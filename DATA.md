# 데이터 출처 및 라이선스 (Data sources & provenance)

재현성을 위해 분석에 사용한 데이터를 저장소에 포함합니다. 아래는 각 데이터의 **원 출처·라이선스**입니다(출처 표기/재배포 조건 준수용).

## 1. COVID-19 공개 데이터셋 (Kaggle)
Kaggle — *Data Science for COVID-19 (DS4C) in South Korea* (by Kim Jihoo)
<https://www.kaggle.com/datasets/kimjihoo/coronavirusdataset>  · License: **CC BY-NC-SA 4.0** (출처 표기·비영리·동일조건)

해당 파일: `Time.csv`, `TimeAge.csv`, `TimeGender.csv`, `TimeProvince.csv`, `Case.csv`, `Policy.csv`, `Region.csv`, `SearchTrend.csv`, `Weather.csv`, `PatientInfo.csv`, `SeoulFloating.csv`

> ⚠️ `PatientInfo.csv` 는 환자 행단위 자료입니다(공개 Kaggle 데이터셋이나 민감 정보). 외부 공유·2차 활용 시 원 라이선스와 개인정보 보호에 유의하세요.

## 2. 외부 자료 (`Data/외부/`)
| 파일 | 내용 | 출처 |
|---|---|---|
| `OnlineCard.csv`, `1920카드소비.csv`, `20192020카드소비.csv` | 월별 온라인 카드 소비 | 공개 카드소비 통계 |
| `한국언론진흥재단_뉴스빅데이터_메타데이터_ESG_*.csv`, `코로나_00.csv`, `train.csv`, `test2.csv` | 뉴스 기사/메타데이터 | 한국언론진흥재단 빅카인즈 <https://www.bigkinds.or.kr> · 공공데이터포털 <https://www.data.go.kr> |
| `negative_words_self.txt`, `positive_words_self.txt` | 감성사전(긍/부정어) | KNU 한국어 감성사전 기반 |
| (자살 통계, 상관분석용) | 월별 자살자 수 | 중앙자살예방센터 데이터존 <https://kfsp-datazoom.org> |

> 뉴스/언론 데이터(빅카인즈)는 이용약관상 재배포가 제한될 수 있습니다. 외부 공개·재사용 전 약관을 확인하세요.

## 3. 통계 재현
헤드라인 통계는 다음으로 재현/확인할 수 있습니다:
```bash
python scripts/verify_stats.py
```
- 부정기사 1.73배 증가: 이표본 비율검정 z=4.11, **p<0.001** (재현됨)
- 월별 카드소비 vs 확진/자살 상관: **N≈6(월)** 기술적 상관 — 유의성 검정 아님, 인과 아님(README 한계 참고)

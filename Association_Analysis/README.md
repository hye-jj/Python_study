
## 연관 분석(Association Analysis)
<img width="412" height="105" alt="image" src="https://github.com/user-attachments/assets/77b26a5b-0e46-4c78-b08f-6871daa67b5a" />

> 출처 : https://medium.com/analytics-vidhya/association-analysis-in-python-2b955d0180c 

<br>
### 1. 개요

* **프로젝트명**: Apriori 알고리즘 기반의 장바구니 연관 분석 스터디
* **목적**: 고객의 거래(Transaction) 데이터를 바탕으로 동시 구매 경향이 높은 상품 조합(연관 규칙)을 발굴하고, 이를 통한 Cross-selling(교차 판매) 및 상품 배치 전략 도출
* **사용 툴 및 라이브러리**: `Python`, `Pandas`, `NumPy`, `mlxtend`, `Matplotlib`

<br>

### 2. 데이터셋 및 전처리

#### 1) 데이터셋 정보

* **데이터 출처**: Retail Transaction Dataset
* **데이터 규모**: 총 315건의 거래 데이터 (7개 컬럼)
* **포함 아이템**: Wine, Cheese, Meat, Bread, Eggs, Milk, Diaper, Bagel, Pencil 등 총 9종

#### 2) 데이터 전처리 (One-Hot Encoding)

* **원본 형태**: 행(Row)별로 고객이 구매한 품목들이 나열된 Unstructured Basket Format
* **변환 과정**:
* 전체 거래에서 등장하는 고유 아이템 목록(Itemset) 추출
* Apriori 알고리즘 입력 포맷에 맞추어, 각 거래별 품목 포함 여부를 `0(미구매)`과 `1(구매)`의 이진(Binary) 데이터프레임(`ohe_df`)으로 변환


<br>

### 3. 분석 방법론 (Apriori Algorithm)

#### 1) 연관 규칙 핵심 지표

* **지지도 (Support)**: 전체 거래 중 품목 A와 B가 동시에 포함된 거래의 비율
* **신뢰도 (Confidence)**: 품목 A를 구매했을 때 품목 B도 함께 구매할 조건부 확률
* **향상도 (Lift)**: 품목 A와 B의 구매가 상호 독립일 때 대비, 얼마나 함께 많이 구매되는지의 비중
* $\text{Lift} > 1$: 양의 연관성 (함께 구매될 가능성이 높음)
* $\text{Lift} = 1$: 상호 독립
* $\text{Lift} < 1$: 음의 연관성



#### 2) 파라미터 설정 및 연관 규칙 추출

* **빈도 아이템셋 추출 (`apriori`)**: `min_support = 0.2` (전체 거래의 최소 20% 이상 등장한 아이템셋만 필터링)
* **연관 규칙 도출 (`association_rules`)**: `metric = "confidence"`, `min_threshold = 0.6` (신뢰도 60% 이상의 유의미한 규칙 추출)

<br>

### 4. 주요 분석 결과 및 해석

#### 1) 주요 연관 규칙 예시

| 조건부(Antecedents) | 결론부(Consequents) | 지지도(Support) | 신뢰도(Confidence) | 향상도(Lift) | 해석 |
| --- | --- | --- | --- | --- | --- |
| **{Bagel}** | **{Bread}** | 0.279 | 0.657 | **1.301** | 베이글을 구매한 고객 중 **65.7%**가 빵을 함께 구매함. 단독 구매 대비 함께 구매될 확률이 **1.3배** 높음. |
| **{Milk}** | **{Cheese}** | 0.305 | 0.608 | **1.211** | 우유를 구매한 고객 중 **60.8%**가 치즈를 함께 구매함. (향상도 1.21로 양의 연관성) |
| **{Cheese}** | **{Milk}** | 0.305 | 0.608 | **1.211** | 치즈 구매 고객 역시 우유 구매 비율이 동일하게 높음 (상호 연관성 확인). |

#### 2) 결과 시각화

* **Support vs Confidence Scatter Plot**:
* 지지도와 신뢰도 간의 분포를 시각화하여, 높은 신뢰도와 일정 수준 이상의 지지도를 동시에 만족하는 최적의 규칙들을 직관적으로 식별함.


<br>

### 5. 인사이트 및 활용 방안 

1. **상품 진열 및 동선 최적화**:
* `{Bagel} → {Bread}`, `{Milk} ↔ {Cheese}` 등 향상도($\text{Lift} > 1$)가 높은 품목군을 매장에서 인접 배치하여 고객 구매 편의성 증대.


2. **번들 상품 및 프로모션 기획**:
* 베이글과 빵, 우유와 치즈를 결합한 할인 묶음 상품(Bundle Pack)을 기획하여 객단가 상승 유도.


3. **온라인 추천 시스템 적용**:
* 장바구니에 '베이글'을 담았을 때 '빵'을 연관 추천 상품으로 노출하는 팝업/추천 로직 구현.


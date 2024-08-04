## Synthetic data

스터디 목적 : 
연구 목적이나 교육 목적으로 사용할 수 있는 공개된 신용 정보와 관련된 데이터를 찾아서 합성데이터를 생성해보는 것을 목표로 합니다.

### 데이터셋
#### CTGAN 실습 무료 데이터셋 
1. UCI Machine Learning Repository             
- 설명: UCI Machine Learning Repository는 다양한 종류의 데이터셋을 제공합니다. 학습, 테스팅 및 연구 목적으로 널리 사용됩니다.
- 추천 데이터셋:
**Adult Data Set** (인구조사 소득 데이터셋): 성별, 연령, 교육, 직업 등 다양한 특성을 포함하고 있으며, 소득 수준을 예측하는 데 사용될 수 있습니다. 이 데이터셋은 범주형과 연속형 변수가 혼합되어 있어 CTGAN 실습에 적합합니다.
- 웹사이트 링크: Adult Data Set(https://archive.ics.uci.edu/dataset/2/adult)         

2. Kaggle
- 설명: Kaggle은 데이터 과학자들이 데이터셋을 공유하고, 다양한 데이터 과제에 참여할 수 있는 플랫폼입니다. 많은 데이터셋이 무료로 제공되며, 사용자가 직접 데이터를 업로드하고 다운로드할 수 있습니다.
- 추천 데이터셋:
Titanic: Machine Learning from Disaster: 타이타닉호 승객 목록을 사용한 생존 예측 데이터셋으로, 나이, 성별, 티켓 등급 등의 특성을 포함합니다. 범주형 데이터의 처리 방법을 실습하기 좋습니다.
- 웹사이트 링크: Titanic Dataset(https://www.kaggle.com/competitions/titanic)      

3. Google Dataset Search
- 설명: Google Dataset Search는 인터넷 상의 다양한 데이터셋을 검색할 수 있는 도구입니다. 공공 데이터부터 학술 데이터까지 광범위하게 검색 가능합니다.
- 사용 방법: 원하는 키워드(예: "health data", "economic data")로 검색하여 관련 데이터셋을 찾을 수 있습니다.
- 웹사이트 링크: Google Dataset Search(https://datasetsearch.research.google.com/)     

4. OpenML
- 설명: OpenML은 다양한 종류의 데이터셋을 공유하는 플랫폼입니다. 기계학습 알고리즘 테스트와 벤치마킹을 위한 데이터셋이 많이 포함되어 있습니다.
- 웹사이트 링크: OpenML(https://www.openml.org/search?type=data&status=active&id=43489)                  


#### 기타 데이터셋 :
1. UCI Machine Learning Repository             
설명: UCI의 기계 학습 저장소에는 다양한 연구 목적으로 사용할 수 있는 데이터 세트가 포함되어 있으며, 여기에는 신용 평가 데이터 세트도 포함됩니다.
특징: 데이터 세트는 주로 신용 카드 신청자의 승인 여부와 관련된 속성을 포함합니다.                
웹사이트 링크: UCI Machine Learning Repository, "German Credit Data"      
<br>
2. Kaggle
설명: Kaggle은 다양한 데이터 과학 대회를 주최하며, 이를 위해 다양한 데이터 세트를 제공합니다. 여기에는 신용 평가와 관련된 데이터 세트도 포함됩니다.
특징: Kaggle 데이터 세트는 종종 신용 정보, 사용자 행동 데이터 등 다양한 특징을 포함합니다.          
웹사이트 링크: Kaggle Datasets, "Home Credit Default Risk"(https://www.kaggle.com/competitions/home-credit-default-risk)
<br>
3. Federal Reserve Economic Data (FRED)
설명: FRED는 경제 데이터를 제공하는 미국 연방준비은행의 데이터베이스입니다. 신용 카드 부채, 대출 비율 등과 같은 매크로 경제적 신용 데이터를 제공합니다.
특징: 데이터는 경제 지표로서의 신용 정보를 포함하며, 시간에 따른 추이를 분석할 수 있습니다.
웹사이트 링크: Federal Reserve Economic Data - FRED(https://fred.stlouisfed.org/)
<br>
4. Consumer Financial Protection Bureau (CFPB)
설명: CFPB는 미국 소비자 금융 보호국으로, 다양한 소비자 금융 데이터를 공개합니다. 이는 신용 카드 불만사항, 대출 데이터 등을 포함할 수 있습니다.
웹사이트 링크: Consumer Financial Protection Bureau
(https://www.consumerfinance.gov/data-research/)
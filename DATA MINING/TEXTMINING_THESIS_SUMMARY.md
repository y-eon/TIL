## Data and Methodology

###### 서론

- 감성 분석 : 주관적 정보(의견, 태도)를 뽑아내고 탐지하는 일련의 기술, 방법

  -> 감성 분석이 흥하게 된 이유는 컴퓨터의 발전과 웹 텍스트의 사용 가능성 때문

- 감성 분석의 단계

  1) 자료 준비(interests)

  2) 전처리

  3) 변수 선택

  4) 양극/ 감성 분류(변수)

  5) 문장/ 문서의 감성 measure

  

#### step 1_Preparing the Corpus(자료준비)

- 1.1) MPB Minutes : 금융 통화 위원회 회의록
  - 섹션 2와 3만 사용
  - 섹션1 : 개요_행정적인 세부사항 제공
  - 섹션2 :  경제상황에 대한 요약_금통위 안에서 논의(경제상황, FX, 국제 금융, 금융 시장, 통화정책)
  - 섹션3 : 통화정책에 대한 논의_개인의 생각 기록?녹음
  - 섹션4: 결론_통화정책 전달
- 1.2) 뉴스 기사
  - 금리를 포함하는 뉴스
  - 신문사 3개 ( 연합뉴스, 이데일리, 연합인포맥스)
    - 기사 복제가 많기 때문에 originator 사용)
- 1_3) 채권분석보고서
  - 자료를 사용한 이유
    - 1. 통화정책과 채권 시장에 대한 전문가 의견이 있기 때문
      2. lexicon에 저널보다는 편안한 어투를 추가하기 위해

=> 결론 자료는 사이즈도 크고 다양한 주제를 다루고 있음(table 3)



#### step 2_Pre-processing Texts(텍스트 전처리)

- 2.1) 전형적인 전처리

  - 토큰화

    - 텍스트를 주로 단어로 나눔

  - 정규화

    - 텍스트를  표준 형태로 바꿈

      - removing puctuation : . 방점? 제거
      - stop words removal : it, the, etc 같은거 제거
      - converting numbers to their word equivalent : 숫자를 단어로 변경
      - stemming : 어간 추출 (am -> am, going-> go)
      - lemmatization : 표제어추출 (am -> be)
      - case folding

  - eKoNLPy
  
    - 많은 단어들이 조사와 결합되어 있어 인식이 어려움(spacing)
  
      → 한국어 형태소 분석을 통해 쉽게 처리 가능
  
    - 외국어 명명 규칙 X , Field-specific한 단어
  
      → 웹 경제 사전을 통해 경제, 금융 분야에 대한 용어를 갖춤
  
    - 다수의 동의어 (단어가 늘어날 수록 차원이 커지는 문제 발생
  
      → 1,324 쌍의 동의어를 정의하고, 대체 동의어 기능 지원
  
    - 동사와 형용사의 불규칙 활용이 많아서 n-gram의 차원 폭발하는 문제 발생
  
      → 1,291개의 경제 금융 필드 형용사와 동사의 lemmatization 지원



#### step 3_Feature Selection(특성 선택)

- 모든 words를 사용할 수 없음
- term vector의 dimension을 줄이기 위한 규칙이 필요



- n-grams 의 필요성 

   uni-gram의 경우 문맥을 파악하기 어렵다
   ex)“낮은(부정) + 실업률(부정) = 낮은 실업률(긍정)”

- Long n-grams 의 문제

  긴 n-grams의 경우 over-fitting 문제점 발생

- 차원의 저주(explosion of dimension) 발생

  N이 큰 경우, n-gram 단어 조합이 확률적으로 다른 문서에 등장하지 않을 확률이 높으므로 단어에 극성에 대한 학습이 되지 않음

  (n ≤ 5인 n-gram을 사용하여 n-gram 단어 사전 구축)

#### step 4_Polarity Classification : Market Approach

- 정의

  - 시장 정보를 이용해 단어의 극성을 분류하는 접근법

- 분류 방법

  - Naïve Bayes Classification을 포함한 Machine Learning 사용

- 학습 순서

  - 4백 만개의 데이터 9:1 비율로 나눔(Train/Test)
  - 5-gram을 사용해 각 문장의 feature 선택함
  - 분류기를 학습시키고 정확도를 측정함
  - 학습된 NBC를 통해 도출한 polarity score로 class(hawkish/dovish)를 분류함

- NBC의 성능

  - Average accuracy of NBC : 86%

    (positive precision: 90%, positive recall: 84%, negative precision: 82%, negative recall: 88%)

#### step 4_Polarity Classification : Lexical Approach

- 정의

  - 극성이 분류된 seed word를 통해 극성을 판단하는 비지도 학습 접근법

    (두 개의 단어가 하나의 문맥에서의 빈도를 측정하여 같은 극성을 갖고 있다고 판단함)

- 분류 방법
  
  - PMI 컨셉을 이용해서 seed word와 n-gram사이의 근접도를 측정
- 학습 순서
  - 극성이 분류된 Seed set of word와 n-gram vector를 lexical 그래프에 배치
  - 둘 사이의 근접성을 측정함
  - n-gram이 각 seed set 중 근접성이 가까운 것으로 극성 분류



#### step 4_Polarity Classification : Evaluaion

- 평가 방법
  - Lexicon을 만드는데 사용되지 않은 자료로 평가를 진행

- 평가 데이터
  
- 한국은행 금융통화위원회 의사록 (수동으로 극성 단어로 분류)
  
- 평가 결과

  - Market approach로 생성된 lexicon의 정확도 : 68%

  (positive precision: 63%, positive recall: 75%, negative precision: 74%, negative recall: 62%)

  - Lexical approac로 생성된 lexico의 정확도 : 67%

  (positive precision: 69%, positive recall: 71%, negative precision: 65%, negative recall: 62%)

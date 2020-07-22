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

      








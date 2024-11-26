# GPT-4 및 LLM 개요

## LLM (Large Language Model)
- **LLM**은 문장의 일부를 보고 비어있는 단어를 확률적으로 맞추는 모델입니다.
- 이 모델은 많은 돈과 시간, 그리고 대규모 메모리와 GPU 훈련 자원을 필요로 합니다.
- LLM의 훈련 데이터는 웹상에 존재하는 문서들로부터 이루어지며, 품질 높은 데이터(예: 위키피디아, 뉴스 기사 등)가 주로 사용됩니다. 이 데이터는 코드 예측과 같은 특정 작업에도 사용될 수 있습니다.
- **비지도학습 (Unsupervised Learning)**을 활용하여 훈련됩니다.

### Temperature 개념
- **Temperature**는 0과 100 사이의 값을 가지며, 100에 가까워질수록 생성되는 결과가 더 랜덤해집니다.

## 모델 훈련 예시
예시: "OpenAI transitioned from non-profit to for-profit"
- 13만 토큰: 
  - `['OpenAI', 'transitioned', 'from', 'non-profit']`
  - `['transitioned', 'from', 'non-profit', 'to']`
  - `['from', 'non-profit', 'to', 'for-profit']`
- **Context Window**의 크기는 4가 되어, 3개의 토큰을 보고 1개의 토큰을 예측합니다.

## Word to Vector
딥러닝을 활용한 단어 임베딩(Word Embedding):
- **RNN**, **LSTM**, **Transformer**를 거쳐 발전합니다.
- **One-Hot Encoding**을 사용하여 단어를 숫자로 변환하고, 이를 **N차원 공간 벡터**로 변환하여 단어 간 유사도를 측정합니다.
  - 예: `king: queen = man: woman`

## Generative Pre-trained Transformer (GPT)
- **OpenAI**에서 만든 초거대 언어 모델로, 훈련과 예측을 위한 전용 하드웨어를 사용합니다.
- **GPT-3**와 **GPT-4** 두 가지 주요 모델을 제공합니다:
  - **Word Completion**: 다양한 언어를 지원하며, 한국어도 포함됩니다.
  - **Code Completion**: GitHub 등의 코드 데이터로 훈련됩니다.

### GPT-3
- 175B 파라미터 (800GB)
- 훈련 비용: $4.6M
- Context Window 크기: 2,048 +1
- 12,288개의 워드벡터 사용

### GPT-4
- 1T 파라미터
- Context Window 크기: 8,192 +1
- 32,768개의 워드벡터 사용
- **Multi-model**: 이미지 인식 기능도 지원

### GPT API
- **Completion**: 
  - Word
  - Code
- **Fine-tuning**: 기존 모델을 나만의 유스케이스에 맞게 조정
- **Whisperer API**
- **ChatGPT API**

## 경량 LLM 모델들
- **Meta**의 **Llama**
- **Stanford**의 **Alpaca**
- **Databricks**의 **Dolly**

## LLM의 문제점
- 훈련 비용과 서빙 비용이 매우 큼.
  - 이로 인해 많은 탄소 배출과 지구 온난화 가속화 문제 발생.
  - GitHub Copilot의 경우 사용자당 20불의 손실 발생 (2023년 10월 기준).
- 많은 기업들이 자체 하드웨어 개발을 진행 중이며, 반도체 산업의 중요성이 증가하고 있음.
- **데이터 주권** 문제: 훈련에 사용된 데이터의 소유권과 관련된 문제가 존재.
- **사회적 문제**: 일자리와 같은 사회 안전성에 영향을 미칠 수 있음.

## ChatGPT 소개
- **2022년 11월 30일** 발표
- GPT 모델을 **Fine-Tuning**하여 챗봇 형태로 활용.
  - **RLHF (Reinforcement Learning from Human Feedback)**: 사람의 피드백을 기반으로 모델을 학습시킴.

### ChatGPT 용도
- 질문에 대한 답변
- 정보 추출 및 요약
- 번역
- 대화 생성
- 글쓰기 지원
- 코드 생성 및 리뷰

### ChatGPT 훈련 과정
1. **답변 지도 학습**: 사람이 만든 질문-답변 데이터를 훈련하여 모델이 학습.
2. **보상 모델 훈련**: AI가 생성한 답변 중 사람이 선호하는 답변을 기준으로 평가.
3. **강화 학습**: AI는 보상 모델을 따라가며 최적의 답변을 생성하도록 학습.

## 파인 튜닝 (Fine-tuning)
기존 모델 위에 새로운 레이어를 얹어, 특정 용도에 맞는 데이터로 훈련하는 방식입니다.
- **ChatGPT**가 대표적인 예입니다.
- GPT는 API로 이를 지원하며, 사용자는 나만의 모델을 생성할 수 있습니다.

## RAG (Retriever-Augmented Generation)
1. **인덱싱 단계**: LLM에 제공할 추가 정보를 Vector DB에 저장합니다.
2. **검색 단계**: 사용자 질문이 들어오면 DB에서 관련 콘텐츠를 검색하여 추출합니다.
3. 추출된 콘텐츠와 질문을 결합하여 프롬프트를 생성하고, LLM에 전달하여 결과를 받습니다. 결과를 후처리하여 사용자에게 전송합니다.

## 질문(Prompt)의 중요성
- **일반적인 질문**: "삼성전자 휴대폰 판매량을 알려줘."
- **세부적인 질문**: "삼성전자 휴대폰 판매량을 2018년부터 분기별로 달러로 알려줘."

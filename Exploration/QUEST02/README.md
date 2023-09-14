# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 이진영
- 리뷰어 : 박근수


# PRT(PeerReviewTemplate) 
- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 노드에서 진행되었던 추출적 및 추상적 요약이 모두 노드와 동일한 프로세스로 잘 이루어 짐
    
- [X]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 전체 코드 블럭에 주석이 잘 달려있어 가독성과 이해되는 부분이 매우 좋습니다.
        
- [X]  **3. 에러가 난 부분을 디버깅하여 문제를 “해결한 기록을 남겼거나” 
”새로운 시도 또는 추가 실험을 수행”해봤나요?**
    - 추출 요약이 전처리한 데이터로 나오지 않았고 이를 원본데이터 사용을 통해 다시 시도하여 성공하는 과정이 잘 담겨있음
```
추출 요약이 나오지 않는 이유에서는 여러가지가 있다.
너무 짧거나 단순한 구조를 가지고 있는 경우.
텍스트의 내용이 너무 일관되거나 반복되는 경우
그렇기에 전처리한 데이터가 아닌 원본 데이터로 다시 시도해보자

extractive_data = pd.read_csv('news_summary_more.csv', encoding='iso-8859-1')
from summa.summarizer import summarize
print("원문 :", data['text'][0])
print("실제요약 :", data['headlines'][0])
print("추출요약 :", summarize(extractive_data['text'][0], ratio=0.5))

원문 : saurav kant alumnus upgrad iiit pg program machine learning artificial intelligence sr systems engineer infosys almost years work experience program upgrad degree career support helped transition data scientist tech mahindra salary hike upgrad online power learning powered lakh careers
실제요약 : upgrad learner switches to career in ml al with salary hike
추출요약 : upGrad's Online Power Learning has powered 3 lakh+ careers.
원본데이터로 진행하니 추출요약을 성공했다.
추출적 요약에서는 전처리한 데이터로는 요약하기 쉽지 않다는 걸 알아냈다
```
        
- [X]  **4. 회고를 잘 작성했나요?**
    - 추가적인 공부의 필요성과 데이터 전처리의 어려움에 대해서 잘 작성하였습니다.

- [X]  **5. 코드가 간결하고 효율적인가요?**

코드는 Python 스타일 가이드를 준수하고 있습니다. 아래는 코드 개선 사항입니다:

중복 모듈 제거: import nltk가 중복되어 있으므로 한 번만 가져오도록 수정하세요.

불필요한 모듈 제거: import urllib.request가 중복되어 있으므로 한 번만 가져오도록 수정하세요.

패키지 버전 표시: 사용하는 패키지의 버전을 주석 등을 사용하여 표시하세요.

TensorFlow와 관련된 경고 숨기기: TensorFlow와 관련된 경고 메시지를 숨기기 위한 경고 필터링 코드를 추가하세요.

이러한 개선 사항을 적용하면 코드의 가독성과 유지 보수성이 향상됩니다. 코드의 일부가 생략되어 있으므로 실제 코드에 적용하기 전에 코드의 전체 부분을 확인하고 수정해야 합니다.


  
# 참고 링크 및 코드 개선
위 중복모듈 제거 및 패키지 버전등을 수정한 코드입니다.

```python
import nltk
from importlib.metadata import version
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import urllib.request
import warnings

# 경고 숨기기
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# 패키지 버전 표시
print("NLTK Version:", nltk.__version__)
print("TensorFlow Version:", version('tensorflow'))
print("Pandas Version:", pd.__version__)
print("Summa Version:", version('summa'))

# 기타 라이브러리 및 함수 정의

# ...

# 파일 다운로드와 관련된 예외 처리
try:
    urllib.request.urlretrieve("https://raw.githubusercontent.com/sunnysai12345/News_Summary/master/news_summary_more.csv", filename="news_summary_more.csv")
    data = pd.read_csv('news_summary_more.csv', encoding='iso-8859-1')
except Exception as e:
    print("파일 다운로드 또는 읽기 오류:", str(e))

# 데이터 전처리 함수 및 다른 함수 정의

# ...

# 모델 학습 및 예측 부분

# ...

# 예제 출력

# ...

```

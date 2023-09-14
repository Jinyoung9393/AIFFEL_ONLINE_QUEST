# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 이진영
- 리뷰어 : 박근수


# PRT(PeerReviewTemplate) 
- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - Raznet50 모델이 적절히 활용됨
    - loss, accuracy 그래프를 통해 학습이 잘 진행되었음을 확인
    - 마지막 블럭 accuracy 92% 달성하였음
    - 총 3개 중 3개 루브릭 만족함
    
- [X]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 전체 코드 블럭에 주석이 잘 달려있어 가독성과 이해되는 부분이 매우 좋습니다.
    - 코드 블록 및 기능마다 주석이 잘 달려있어 이해하기 쉬웠습니다.
        
- [X]  **3. 에러가 난 부분을 디버깅하여 문제를 “해결한 기록을 남겼거나” 
”새로운 시도 또는 추가 실험을 수행”해봤나요?**
    - 리뷰하는 과정을 통해 VGG16 모델을 생성 후 개선을 통하여 Raznet50 모델을 생성함을 인지함
    - 해당 모델의 개선을 위하여 배치사이즈 및 사전 훈련 가중치 고정 등을 적절히 수행하였습니다.
    ```python
    # 사전 훈련된 가중치를 고정
    for layer in base_model.layers:
    layer.trainable = False
    ```
        
- [X]  **4. 회고를 잘 작성했나요?**
    - 전반적인 흐름에 대한 주석이 잘 작성되어 있었으며 전체 모델에 대한 시각화를 통해 raznet 모델에 대하여 이해하기 쉬웠습니다.
    - plot_model(model, to_file='flower_classification_resnet.png', show_shapes=True)  # 모델 시각화 및 저장
        - 위 코드를 통해 전체 모델의 설계를 한눈에 볼수 있었습니다

- [X]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
        - 들여쓰기: 코드가 들여쓰기가 잘되어 있어서 좋습니다. 그런데 epochs=epochs; 줄에 들여쓰기 오류가 있습니다. 세미콜론(;)은 쉼표(,)로 바꿔야 합니다.
        - 가져오기: import 문이 올바르게 구성되어 있으며 표준 라이브러리 가져오기, 타사 라이브러리 가져오기 및 자체 모듈 가져오기를 분리하는 권장 스타일을 사용하고 있습니다.
        - 주석: 코드에 주석이 잘 달려 있어 가독성과 이해가 좋습니다.
        - Docstring: 함수에 대한 Docstring이 없습니다. 일반적으로 각 함수가 수행하는 작업, 인수, 반환 내용을 설명하기 위해 독스트링을 포함하는 것이 좋습니다.
        - 코드 구조: 코드 구조는 논리적이며 데이터 로드 및 시각화, 데이터 사전 처리, 모델 생성, 교육 및 평가를 위한 별도의 섹션이 있습니다.
        - 플로팅: 플로팅에 'matplotlib'을 사용하고 있으며 플롯을 생성하고 표시하는 코드가 올바르게 보입니다.

    -전반적으로 코드는 잘 작성되었으며 Python 스타일 가이드를 준수합니다. 
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 모듈화(함수화) 했는지
        - 코드 확인 시 중복되는 코드가 없이 잘 작성되어 있습니다.
  
# 참고 링크 및 코드 개선
```python
# 코드 리뷰 시 참고한 링크가 있다면 링크와 간략한 설명을 첨부합니다.
# 모델 훈련의 세미콜론: 모델을 훈련시키는 줄에 작은 오타가 있습니다. 쉼표(,) 대신 세미콜론(;)이 있습니다. epochs=epochs; 대신 epochs=epochs여야 합니다.
# 시각화 루프: 처음 5개의 이미지를 시각화하는 루프에서 plt.show() 뒤에 break 문을 추가하여 첫 번째 반복 후에 루프가 종료되도록 하는 것이 좋습니다.
# 플로팅 함수: matplotlib.pyplot을 두 번 가져왔습니다. 한 번만 가져오면 됩니다.

# 수정된 코드
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model
import matplotlib.pyplot as plt

# ... (rest of your code) ...

def preprocess_data(data):
    """
    Preprocesses data for training.

    Args:
        data (dict): Dictionary containing 'image' and 'label'.

    Returns:
        tuple: Tuple containing preprocessed image and one-hot encoded label.
    """
    # ... (rest of your code) ...

# ... (rest of your code) ...

# Training the model
epochs = 10

history = model.fit(
    train_batches,
    epochs=epochs,
    validation_data=validation_batches
)

# ... (rest of your code) ...

# Model evaluation
test_loss, test_accuracy = model.evaluate(test_batches)
print(f'Test Loss: {test_loss:.4f}')
print(f'Test Accuracy: {test_accuracy:.4f}')
```

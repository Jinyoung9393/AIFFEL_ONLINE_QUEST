# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 이진영
- 리뷰어 : 이윤상


# PRT(PeerReviewTemplate) 
각 항목을 스스로 확인하고 토의하여 작성한 코드에 적용합니다.

- [X] 코드가 정상적으로 동작하고 주어진 문제를 해결했나요?
  
- [X] 주석을 보고 작성자의 코드가 이해되었나요?
  > 각각의 코드마다 어떤 동작을 하는지 구체적으로 명시되어있습니다.
- [X] 코드가 에러를 유발할 가능성이 없나요?
  > 리스트가 바뀌어도 코드가 정상적으로 동작하게 될 것입니다.
- [X] 코드 작성자가 코드를 제대로 이해하고 작성했나요?
  > 네. 몇번의 질문을 했고 명확하게 대답해주셨습니다.
- [X] 코드가 간결한가요?
  > 함수와 for문을 적절하게 사용하여 간결한 코드를 만들었습니다.

# 예시
1. 코드의 작동 방식을 주석으로 기록합니다.
2. 코드의 작동 방식에 대한 개선 방법을 주석으로 기록합니다.
3. 참고한 링크 및 ChatGPT 프롬프트 명령어가 있다면 주석으로 남겨주세요.
```python
from time import sleep as sl    # time 모듈에서 sleep 함수를 가져오고 sl로 이름을 지정한다.

def show_fish_movement_comprehension(fish_list):
  movements_c=[f"{i['이름']} is swimming at {i['speed']}m/s" for i in fish_list] #컴프리헨션을 이용해서 새로운 리스트를 만든다.
  for i in movements_c:                              # 해당값을 2초간격으로 출력하기 위해 for문을 이용해 하나씩 출력한다.
    print(i)
    sl(2)



def show_fish_movement_Generator(fish_list):
    def generate_movements():                               # 제너레이터 함수를 만든다.
        for i in fish_list:                                 # 임의의 변수에 원하는 출력값을 저장 후 반환한다.
            yield f"{i['이름']} is swimming at {i['speed']}m/s."


    movements = generate_movements()                        # 변수선언을 통해 제너레이터를 바인딩한다.
    for i in movements:                                     # next() 대신에 for문으로 제너레이터 함수를 2초 간격으로 출력한다.
        print(i)
        sl(2)

fish_list = [{"이름":"Nemo", "speed":3},{"이름":"Dory", "speed": 5}]


print("Using Comprehension:")
show_fish_movement_comprehension(fish_list)
print("Using Generator:")
show_fish_movement_Generator(fish_list)
```

# 참고 링크 및 코드 개선
```python
from time import sleep as sl    # time 모듈에서 sleep 함수를 가져오고 sl로 이름을 지정한다.

def show_fish_movement_comprehension(fish_list):
  movements_c=[f"{i['이름']} is swimming at {i['speed']}m/s" for i in fish_list] #컴프리헨션을 이용해서 새로운 리스트를 만든다.
  for i in movements_c:                              # 해당값을 2초간격으로 출력하기 위해 for문을 이용해 하나씩 출력한다.
    print(i)
    sl(2)



def show_fish_movement_Generator(fish_list):
    def generate_movements():                               # 제너레이터 함수를 만든다.
        for i in fish_list:                                 # 임의의 변수에 원하는 출력값을 저장 후 반환한다.
            yield f"{i['이름']} is swimming at {i['speed']}m/s."


    movements = generate_movements()                        # 변수선언을 통해 제너레이터를 바인딩한다.
    while True:                                                               # next() 함수를 이용하기 위해 while True를 이용해서 무한하게 반복문을 시행합니다.
        try:
            sl(2)
            fish_movement = next(movements)                                   # next()함수를 이용해서 yield값을 차례대로 출력합니다.
            print(fish_movement)
        except StopIteration:                                                  # 제너레이터에서 더 이상 반환한 값이 없을때 break를 시행합니다.
            break

fish_list = [{"이름":"Nemo", "speed":3},{"이름":"Dory", "speed": 5}]


print("Using Comprehension:")
show_fish_movement_comprehension(fish_list)
print("Using Generator:")
show_fish_movement_Generator(fish_list)
```

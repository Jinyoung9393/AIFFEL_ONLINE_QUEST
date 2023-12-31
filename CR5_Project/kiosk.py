menu = ['americano', 'latte', 'mocha', 'yuza_tea', 'green_tea', 'choco_latte']
price = [2000, 3000, 3000, 2500, 2500, 3000]
class Kiosk:
    def __init__(self):
        self.menu = menu
        self.price = price
    def menu_print(self):
        for i in range(len(self.menu)):
            print(i + 1, self.menu[i], ' : ', self.price[i], '원')

    def menu_select(self):
        self.order_menu = []  
        self.order_price = []  

        n = 0
        while n < 1 or len(menu) < n:
            n = int(input("음료를 번호를 입력하세요 : "))  

            # 메뉴판에 있는 음료 번호일 때
            if 1 <= n & n <= len(menu):
                self.order_price.append(self.price[n-1])  
                self.price_sum = self.price[n-1] 
            else:
                print("없는 메뉴입니다. 다시 주문해 주세요.")

        # 음료 온도 물어보기
        t = 0  # 기본값을 넣어주고
        while t != 1 and t != 2:  # 1이나 2를 입력할 때까지 물어보기
            t= int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
            if t == 1:
                self.temp = "HOT"
            elif t == 2:
                self.temp = "ICE"
            else:
                print("1과 2 중 하나를 입력하세요.\n")

        self.order_menu.append(self.temp + ' ' + self.menu[n-1])  # 주문 리스트에 추가합니다.
        print(self.temp, self.menu[n-1], ' : ', self.price[n-1], '원')  # 온도 속성을 추가한 주문 결과를 출력합니다.

  
        while n != 0:  
            print()  
            n = int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요 : "))
            if n > 0 and n < len(self.menu) + 1:
                self.order_price.append(self.price[n-1]) 
                self.price_sum += self.price[n-1]  # 합계 금액
                t = 0  # 기본값을 넣어주고
                while t != 1 and t != 2:  # 1이나 2를 입력할 때까지 물어보기
                    t= int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
                    if t == 1:
                        self.temp = "HOT"
                    elif t == 2:
                        self.temp = "ICE"
                    else:
                        print("1과 2 중 하나를 입력하세요.\n")
                self.order_menu.append(self.temp + ' ' + self.menu[n-1])
                print('추가 주문 음료', self.temp, self.menu[n-1], ':', self.price[n-1], '원\n', '합계 : ', self.price_sum, '원')
            elif n == 0 :
                print("주문이 완료되었습니다.")
                print(self.order_menu, self.order_price)  # 확인을 위한 리스트를 출력합니다.
            else : 
                print("없는 메뉴입니다. 다시 주문해 주세요.")

    def pay(self):
        print(f"총 합계 금액은 {self.price_sum}입니다.")
        n=0
        while n != 1 and n !=2:
            n = int(input('현금결제는 1번, 카드결제는 2번을 눌러주세요'))
            if n ==1:
                print('직원을 호출하겠습니다.')
            elif n ==2:
                print('IC칩 방향에 맞게 카드를 꽂아주세요.')
            else:
                print('다시 결제를 시도해 주세요.')
    def table(self):

        print('⟝' + '-' * 30 + '⟞')
        print('|' + ' ' * 31 + '|')
        print('|' + ' ' * 31 + '|')
        print('|' + ' ' * 31 + '|')
        print('|' + ' ' * 31 + '|')
        for i in range(len(self.order_menu)):
            print(self.order_menu[i - 1], ' : ', self.order_price[i - 1])
        print('합계 금액 :',sum(price))
        print('|' + ' ' * 31 + '|')
        print('|' + ' ' * 31 + '|')
        print('|' + ' ' * 31 + '|')
        print('|' + ' ' * 31 + '|')
        print('⟝' + '-' * 30 + '⟞')
a = Kiosk()  
a.menu_print()  
a.menu_select()  
a.pay()  
a.table()  

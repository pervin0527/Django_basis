class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print("hello")

    def report(self):
        print(f"I am {self.first_name}, {self.last_name}")

class Agent(Person):
    def __init__(self, first_name, last_name, code_name):
        super().__init__(first_name, last_name) ## 부모 클래스의 생성자를 기반으로 더 많은 속성을 추가(확장)하기 위함.
        self.first_name = first_name
        self.last_name = last_name
        self.code_name = code_name

    def report(self): ## Method Override
        print("Hell Sir!")

    def reveal(self, passcord):
        if passcord == 123:
            print(f"{self.code_name}")
        else:
            self.report()

man1 = Person("John", "Smith")
man1.report()
# man1.reveal() ## 부모 클래스의 인스턴스이므로 자식 클래스의 메서드를 사용할 수 없다.

man2 = Agent("Kyle", "Moore", code_name="ZICO")
man2.hello()
man2.reveal(passcord=123)
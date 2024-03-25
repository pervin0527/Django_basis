a, b = 10, 10

try:
    c = a + b
except:
    print("except 블록은 try 블록에서 발생한 예외를 처리.")
else:
    print("else 블록은 try 블록 내의 코드가 예외 없이 성공적으로 실행됐을 때 실행.")
finally:
    print("finally 블록은 예외 발생 여부와 관계없이 실행되는 코드.")
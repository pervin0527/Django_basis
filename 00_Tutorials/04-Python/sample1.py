test = "this is sentence."
# test[0] = "J" ## 문자열은 Immutable.

print(test)

test2 = test[0:4] # slicing은 start : end-1까지 가져온다.
print(test2)

input_string = "I love programming with python!" ## 두번째 단어를 모두 대문자로 바꾸고 출력.

# target = input_string[2:6].upper()
# input_string[2:6] = target ## immutable.

words = input_string.split()
words[1] = words[1].upper()
words = " ".join(words)
print(words)

sample_dict = {"key1" : 100, "key2" : 200, "key3" : 300}
sample_dict.update({"key4" : 400})
for k, v in sample_dict.items():
    print(k, v)
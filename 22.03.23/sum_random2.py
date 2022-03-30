# 문제는 두 자릿수 덧셈으로만 출제
# 5문제 출제
# 시간 출력
# 5문제를 푸는데 10초가 안 걸렸으면 "참 잘했어요" 출력하기

import random
import time

start = time.time()
for x in range(5):

    a = random.randint(10,99)
    b = random.randint(10,99)

    print(x+1, "번째 문제", a, "+", b, "=")
    x = input()
    c = int(x)

    if a+b == c:
        print("맞았습니다!\n")
    else:
        print("틀렸습니다.\n")


end = time.time()
print("문제가 모두 끝났습니다")
print("걸린 시간 : ", end-start, "초")


if end-start < 10:
    print("참 잘했어요!")
else:
    print("좀 더 노력하세요")

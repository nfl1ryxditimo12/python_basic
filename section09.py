# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대경로 

# 파일 읽기

# 예제1

f = open('./resource/review.txt', 'r')
# 변수 = 연다('./주소', 'r = read')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()

print("\n=====================================\n")

# 예제 2

with open('./resource/review.txt', 'r') as f:
# with 구문은 close() 함수를 사용하지 않아도 알아서 종료된다.
# as 로 긴 문장을 f에 담는다.
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print("\n=====================================\n")

# 예제 3

with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())
        # 공백 없이 모든 문장을 출력한다.

print("\n=====================================\n")

# 예제 4

with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)

    # 내용 없음
    content = f.read()
    print(">", content)
    # 파일을 두 번째 불러오면 내용이 없어서 안불러와진다.

print("\n=====================================\n")

# 예제 5

with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # readline() 함수는 한 줄만 불러와 진다.
    # print(line)
    while line:
        print(line, end='####')
        line = f.readline()
        # while 문으로 반복실행 하게 되면 다 불러와진다
        # 마지막에 readline()을 한번 더 실행해야 함

print("\n=====================================\n")

# 예제 6

with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    # readlines() 함수는 모든 문장을 리스트로 변경 하고
    # 한 문장 마다 인덱스를 부여한다.
    print(contents)

    for c in contents:
        print(c, end=' ******* ')

print("\n=====================================\n")

# 예제 7

# f = open('./resource/score.txt', 'r')
# list_f = f.readlines()
# sum = 0
# avg = 0
# len1 = 0
# for i in list_f:
#     int_f = int(i)
#     sum += int_f
#     len1 = len(list_f)

# avg = sum / len1
# print(avg)
# f.close()

with open('./resource/score.txt', 'r') as f:
    score = []                                                      # 리스트 생성
    for line in f:                                                  # 파일의 값들을 for 문으로 하나씩 불러옴
        score.append(int(line))                                     # score 리스트에 파일 값들을 순차적으로 집어넣음
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))             # score 리스트 안의 값들의 평균을 냄

print("\n=====================================\n")

# 파일 쓰기

# 예제 1

with open('./resource/text1.txt', 'w') as f:                        # 파일 읽기는 r 쓰기는 w 추가는 a 로 이루어진다.
    f.write('Niceman!\n')

# 예제 2

with open('./resource/text1.txt', 'a') as f:                        # 파일 추가
    f.write('Goodman!\n')

# 예제 3

from random import randint                                          # 랜덤함수 생성

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))                                # 1 - 49 까지의 무작위 수를 문자열 형식으로 파일에 쓴다.
        f.write('\n')

# 예제 4
# writelines : 리스트 -> 파일로 저장

with open('./resource/text3.txt', 'w') as f:
    list = ['kin\n', 'Park\n', 'Cho\n']                             # 리스트를 파일에 쓴다
    f.writelines(list)

# 예제 5

with open('./resource/text4.txt', 'w') as f:
    print('Test Contents1!', file=f)                                # print 함수로도 파일 쓰기가 가능하다
    print('Test Contents2!', file=f)
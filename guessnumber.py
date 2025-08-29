import random

answer_digit=random.sample(range(0,10),4)
answer=''.join(str(d) for d in answer_digit)
guess_count=0
max_count=10
while guess_count<max_count:
    guess=input("請輸入4位數字(0~9,數字不能重複)或輸入Q離開遊戲:")
    A_count=0
    B_count=0
    if len(guess)==4 and guess.isdigit():
        guess_digit=[int(guess[i]) for i in range(4)]
        B_match=0
        for i in range(4):
            if guess_digit[i]==answer_digit[i]:
                A_count+=1
        for i in range(4):
            if guess_digit[i] in answer_digit:
                B_match+=1
        B_count=B_match-A_count
        print(f"猜測{guess}:{A_count}A{B_count}B")
        guess_count+=1
        if A_count==4:
            print(f"答對了!答案是{answer}")
            break
    elif guess=="Q":
        break
    else:
        print("輸入錯誤數字!")
if guess_count>=10 and A_count<4:
    print(f"遊戲結束!答案是{answer}")
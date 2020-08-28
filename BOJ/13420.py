for i in range(int(input())):
    A,B=input().replace(' ','').split("=")
    if eval(A)==int(B):
        print("correct")
    else:
        print("wrong answer")
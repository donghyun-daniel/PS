def solution(name):
    name=list(map(lambda x: ord(x)-65, name))
    ans=len(name)-name.count(0)
    move=0
    cursor=0
    while True:
        if name[cursor]: #문자 조정 및 횟수
            move+=min(26-name[cursor], name[cursor])
            name[cursor]=0
            ans-=1
        if ans==0:
            return move
        for i in range(1,len(name)//2+2): #위치바꾸기
            move+=1
            if name[cursor+i]:
                cursor += i if cursor+i<len(name) else i-len(name)
                break
            if name[cursor-i]:
                cursor -= i if cursor-i else i+len(name)
                break
def solution(answers):
    an=[]
    answer = [0 for _ in range(3)]
    #수포자 답안 패턴
    dic={1:[1,2,3,4,5],2:[2,1,2,3,2,4,2,5],3:[3,3,1,1,2,2,4,4,5,5]}
    
    #수포자 한 명씩 보기
    for i in dic.keys():
        # i변째 수포자가 작성한 답안지 만들기
        colab=dic[i]*(len(answers)//len(dic[i]))+dic[i][:len(answers)%len(dic[i])]
        
        #탐색 (답지와 비교)
        for j,k in zip(answers,colab):
            if j==k: #같다면
                answer[i-1]+=1
                
    #가장 높은 점수 받은 사람 추출
    for i,j in enumerate(answer):
        if j == max(answer):
            an.append(i+1)
    return an
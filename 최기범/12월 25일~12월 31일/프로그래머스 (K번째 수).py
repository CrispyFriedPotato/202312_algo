def solution(array, commands):
    answer = []
    copy_array = array
    for i in commands : 
        array = copy_array
        array = array[i[0]-1 : i[1]]
        array.sort()
        answer.append(array[i[2]-1])
    return answer
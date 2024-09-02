def solution(my_strings, parts):
    answer = ''
    for i, part in enumerate(parts):
        s, e = part  # 시작 인덱스와 끝 인덱스 추출
        substring = my_strings[i][s:e+1]  # 부분 문자열 추출
        answer += substring  # 추출한 부분 문자열을 정답에 추가
    return answer

    

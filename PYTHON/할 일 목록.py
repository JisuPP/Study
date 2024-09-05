def solution(todo_list, finished):
    check = list(zip(todo_list, finished))
    ans = []

    for todo, finish in check:
        if finish == False:
            ans.append(todo)
    return ans

############################################

def solution(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]

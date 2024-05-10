def solution(board):
    n = len(board)
    not_safe = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                not_safe = not_safe + 1
            else:
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                            if x == 0 and y == 0:
                                 continue
                            else:
                                ix = i + x
                                jy = j + y
                                if (0 <= ix < n) and (0 <= jy <n) and board[ix][jy] == 1:
                                    not_safe = not_safe + 1
                                    break
                                    
    return (n*n) - not_safe

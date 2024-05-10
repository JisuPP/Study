def solution(board):
    
    num_o = sum(row.count("O") for row in board)
    num_x = sum(row.count("X") for row in board)
    if abs(num_o - num_x) > 1:
        return 0
    
    
    # 가로
    for i in range(3):
        if board[i][0] != '.' and board[i][0] == board[i][1] == board[i][2]:
            return 0
    # 세로
    for j in range(3):
        if board[0][j] != '.' and board[0][j] == board[1][j] == board[2][j]:
            return 0
    # 대각선
    if board[0][0] != '.' and board[0][0] == board[1][1] == board[2][2]:
        return 0
    if board[0][2] != '.' and board[0][2] == board[1][1] == board[2][0]:
        return 0
    
    # 선공과 후공 번갈아가면서 표시했는지 확인
    num_moves = num_o + num_x
    # 선공 O
    if num_moves % 2 == 0:  
        if num_o <= num_x:  
            return 0
    # 후공 X
    else:  
        if num_o > num_x:  
            return 0
    
    return 1
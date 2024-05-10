def solution(storey):
    c = range(-9, 10)
    buttons = [10**b for b in c]
    button_presses = 0

    for button in buttons:
        # 버튼을 누를 수 있는 만큼 누름
        while storey >= button:
            storey -= button
            button_presses += 1

    return button_presses
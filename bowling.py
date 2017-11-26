def score(game):
    totalScore = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        totalScore = ifSpare(game, i, totalScore)
        if frame < 10 and get_value(game[i]) == 10:
            totalScore = getScore(game, i, totalScore)
        in_first_half, frame = decideFirstHalf(in_first_half, frame)
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
    return totalScore


def ifSpare(game, i, totalScore):
    if game[i] == '/':
        last = get_value(game[i - 1])
        totalScore += 10 - last
    else:
        totalScore += get_value(game[i])
    return totalScore


def decideFirstHalf(in_first_half, frame):
    if not in_first_half:
        frame += 1
    if in_first_half:
        in_first_half = False
    else:
        in_first_half = True
    return in_first_half, frame


def getScore(game, i, totalScore):
    if game[i] == '/':
        totalScore += get_value(game[i + 1])
    elif game[i] == 'X' or game[i] == 'x':
        totalScore += get_value(game[i + 1])
        if game[i + 2] == '/':
            totalScore += 10 - get_value(game[i + 1])
        else:
            totalScore += get_value(game[i + 2])
    return totalScore


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char in ('X', 'x', '/'):
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

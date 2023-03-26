def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        endX, endY = ball
        candid = []
        if not (startY == endY and endX < startX):
            candid.append((startX + endX)**2 + abs(endY - startY)**2)
        if not (startY == endY and endX > startX):
            candid.append(((m - startX) + (m - endX))**2 + abs((endY - startY))**2)
        if not (startX == endX and endY < startY):
            candid.append((startY + endY)**2 + abs(endX - startX)**2)
        if not (startX == endX and endY > startY):
            candid.append(((n - startY) + (n - endY))**2 + abs((endX - startX))**2)
        #print(candid)
        answer.append(min(candid))
    return answer
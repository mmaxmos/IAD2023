def HanoiTower(n, fromT, toT):
    if n == 1:
        print(n, fromT, toT)
        return
    unusedT = 6 - fromT - toT
    HanoiTower(n-1, fromT, unusedT)
    print(n, fromT, toT)
    HanoiTower(n-1, unusedT, toT)
HanoiTower(int(input()), 1, 3)

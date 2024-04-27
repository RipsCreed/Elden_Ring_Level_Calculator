lvl = int(input("Input Your Level  :"))
lvl_to = int(input("How Many Levels Will You Skip  :"))

def Calculate_Rune(lvl):
    x = ((lvl + 81) - 92) * 0.02
    Rune_Cost = ((x + 0.1) * ((lvl + 81) ** 2)) + 1
    return Rune_Cost
total_rune_cost = 0
for i in range(lvl_to + 1):
    total_rune_cost += Calculate_Rune(lvl)
    lvl += 1

print(int(total_rune_cost))
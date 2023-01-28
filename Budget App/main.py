import budget

cloth = budget.Category("Cloth")
food = budget.Category("Food")
health = budget.Category("Health")
music = budget.Category("Music")

cloth.deposit(30, "party")
cloth.deposit(30, "graduationgraduationgraduationgraduationgraduation")
cloth.deposit(30, "beach")
cloth.withdraw(40)
cloth.transfer(10, food)

food.deposit(30, "pasta")

music.deposit(20, "headphones")
health.deposit(80, "surgery")

balance = food.get_balance()
#print(cloth.ledger, "||", food.ledger)
#cloth.transfer(10, food)
#print(cloth.ledger, "||",food.ledger)

a = budget.create_spend_chart([cloth, food, music, health])
print(a)
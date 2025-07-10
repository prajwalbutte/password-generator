import random
items = ["Prajwal","Amit","Rajwant","Hari"]

print(random.choice(items))

random.shuffle(items)
print("Random Order : ",items)

winners = random.sample(items,2)
print("winners :",winners)
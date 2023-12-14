import random

option = random.sample(range(1, 5), k=random.randint(0, 4))
option.sort()
print(option)
import random

#random_int = random.randint(1, 10)
#print(random_int)

#random_number_0_to_1 = random.random()
#print(random_number_0_to_1)
# values range from 0 (so inclusive of zero to less than 1)
# a>=0 and b<1

#random_float= random.uniform(1,10)
#print(random_float)
# answers examples: 7.73, 2,366, 9.56
# therefore it can be 10 depending on the rounding

random_integer= random.randint(0,1)
print(random_integer)
if random_integer == 0:
    print("Heads")
else:
    print("Tails")

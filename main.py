import random



random_list = random.sample((2,3,4),2)
print(random_list)


random_number = random.randint(1,1000)
print(random_number)

start_range = random_number - random_list[0]
end_range = random_number + random_list[1]



range_hint = (f'The Number is between {start_range} & {end_range}')
print(range_hint)

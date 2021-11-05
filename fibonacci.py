
first_num = 0
second_num = 1


for i in range(1 , 100):
	sum_num = first_num + second_num
	first_num = second_num
	second_num = sum_num
	print(sum_num)

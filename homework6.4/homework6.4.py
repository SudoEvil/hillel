#Перший спосіб із існуючим списком
# random_list = [2,3, 8, 12, 23, 22, 56, 900, 78 ]
# sum_of_num_list = 0

#Другий спосіб із введенням через input
random_list = list(map(int, input("Введіть декілька чисел через пробіл (наприклад: ʼ1 2 3ʼ): ").split()))
sum_of_num_list = sum( num for num in random_list if num  % 2 == 0)

#Розвернутий варіант виразу вище
# for num in random_list:
#     if num % 2 == 0:
#         sum_of_num_list += num


print("Сума всіх парних чисел - " + str(sum_of_num_list))



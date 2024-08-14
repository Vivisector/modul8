def personal_sum(numbers):
    # result_test = sum(numbers)
    result = 0
    incorrect_data = 0
    for i in range(len(numbers)):
        try:
            result +=numbers[i]
        except TypeError: #as Typerr:
            incorrect_data += 1
            # print(f'Некорректный тип данных в {i+1}-м элементе массива nums - "{numbers[i]}": {Typerr}')
            print(f'Некорректный тип данных для подсчета суммы в {i + 1}-м элементе массива nums - "{numbers[i]}"')
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        res = personal_sum(numbers)
        # result = personal_sum(numbers)[0]/len(numbers) - personal_sum(numbers)[1]
        result = res[0]/(len(numbers) - res[1])
        return int(result) if result == 0 else result
        # return result
    except ZeroDivisionError as ZeroDiv:
        return 0
    except TypeError as Typeerr:
        print('В numbers записан некорректный тип данных')
        return None

print(f'{"":=^20}')
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'{"":=^20}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'{"":=^20}')
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'{"":=^20}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
# exit()
nums=[1,12,34,-124,'test']
# print(f'\nРезультаты вызовов первой функции с другими данными {nums}')
# # print(f'{"":=^20}')
# print(calculate_average(nums))
# print(f'{"":=^20}')
# nums2 = [1, "Строка", 3, "Ещё Строка"]
# print(calculate_average(nums2))





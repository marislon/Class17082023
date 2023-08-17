def main():
    n = int(input("Введите размер массива: "))
    arr = []

    for i in range(n):
        element = float(input(f"Введите элемент {i+1}: "))
        arr.append(element)

    negative_sum = 0
    for num in arr:
        if num < 0:
            negative_sum += num

    arr.sort()  # Сортировка элементов массива по возрастанию

    print("Сумма отрицательных элементов:", negative_sum)
    print("Массив после сортировки:", arr)

if __name__ == "__main__":
    main()

from random import randint

counter = 0

def bubble_sort(arr):
    global counter
    for i in range(0, len(arr)):
        for j in range(len(arr) - 1, i, -1):
            counter += 1
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


if __name__ == "__main__":
    dane = [randint(0, 1000) for element in range(100 * 100)]
    print(dane)
    bubble_sort(dane)
    print(dane)
    print("Counter: ", counter)
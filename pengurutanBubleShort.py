def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

my_list = [64, 25, 12, 22, 11]

sorted_list = bubble_sort(my_list)

print("List setelah diurutkan:", sorted_list)

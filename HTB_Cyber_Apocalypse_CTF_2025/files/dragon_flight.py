
def update(arr, i, x):
    arr[i] = x

def query(arr, l, r):
    max_sum_here = arr[l]
    max_so_far = max_sum_here
    for i in range(l + 1, r + 1):
        max_sum_here = max(max_sum_here + arr[i], arr[i])
        max_so_far = max(max_so_far, max_sum_here)
    
    return max_so_far

def main():
    arr_len, operation_num = map(int, input().split())
    arr = list(map(int, input().split()))[:arr_len]
    for i in range(operation_num):
        input_str_list = input().split()
        op = input_str_list[0]
        n1 = int(input_str_list[1])
        n2 = int(input_str_list[2])
        if op == "U":
            update(arr, n1 - 1, n2)
        elif op == "Q":
            M = query(arr, n1 - 1, n2 - 1)
            print(M)

main()
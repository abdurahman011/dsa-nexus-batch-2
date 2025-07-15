if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    max_arr = max(arr)
    arr.remove(max_arr)
    max_arr = max(arr)
print(max_arr)

def find_unique_triplets(arr):
    n = len(arr)
    arr.sort()
    for i in range (0, len(arr)-1):
            left = i + 1
            right = len(arr) - 1
            present = 0
            while (left < right):

                    if (arr[i] + arr[left] + arr[right] == 0):
                            print ("Unique triplet ",  arr[i] , arr[left] , arr[right])
                            present = 1
                            arr.pop(right)
                            arr.pop(left)
                            arr.pop(i)
                    elif (arr[i] + arr[left] + arr[right] > 0):
                            right -= 1
                    else:
                            left += 1
                    if (present == 1):
                            left = 5
                            right = 0


def main():
        arr = list (map (int, input().split()))
        find_unique_triplets(arr)

if __name__=="__main__": 
    main()
def remove_val(arr, val1, val2, val3):
         arr.remove(val1)
         arr.remove(val2)
         arr.remove(val3)

def find_unique_triplets(arr):
    arr.sort()
    for i in range (0, len(arr)-1):
            left = i + 1
            right = len(arr) - 1
            present = 0
            while (left < right):
                    if (arr[i] + arr[left] + arr[right] == 0):
                            print ("Unique triplet ",  arr[i] , arr[left] , arr[right])
                            present = 1
                            remove_val(arr,  arr[i] , arr[left] , arr[right])
                            break
                    elif (arr[i] + arr[left] + arr[right] > 0):
                            right -= 1
                    else:
                            left += 1
                    if (present == 1):
                            break


def main():
        arr = list (map (int, input().split()))
        while arr:
                print("No input")
        find_unique_triplets(arr)

if __name__=="__main__": 
    main()
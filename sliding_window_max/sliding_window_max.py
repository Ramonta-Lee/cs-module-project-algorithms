'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

As a window 'k' traverses a list
For each element in the list, in the window, at 'k'
get the highest value
return a list with those values

'''
def sliding_window_max(nums, k):
    # Your code here
    
    max = 0
    num2 = []
    
    for i in range(len(nums) - k + 1): # iterates through the list
        max = nums[i] 

        for j in range(1, k): 
            if nums[i + j] > max: 
                max = nums[i + j] 

        num2.append(max)
        

    return num2




    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

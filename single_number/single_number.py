'''
Input: a List of integers where every int except one shows up twice
Returns: an integer

Need to return number that isn't a duplicate
Iterate over list to ensure non-duplicates (check for methods)
Tell it when to stop (for loop does this)
How to check for duplicate? (count method)

'''
def single_number(arr):
    # Your code here
    for elem in arr:
        if arr.count(elem) == 1:
            return elem



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
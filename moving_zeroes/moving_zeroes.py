'''
Input: a List of integers
Returns: a List of integers

iterate over array to see every elem
if elem matches 0 move to the end
shift everything over to fill moved zero
return the altered list
'''
def moving_zeroes(arr):
    # Your code here
    for elem in arr:
        if elem == 0:
            # remove zero from index and append a zero
            # shift everything to the left 1 (happens when you remove elem)
            # increment down the for loop (done by for loop)
            arr.remove(elem)
            arr.append(0)
        
    return arr

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
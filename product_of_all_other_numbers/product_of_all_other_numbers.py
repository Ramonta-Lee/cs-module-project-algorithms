'''
Input: a List of integers
Returns: a List of integers
iterate over the list
multiply all elements together
What happens if an element is a zero??
at each index divide out the value from that total
'''
def product_of_all_other_numbers(arr):
    # Your code here
    product = 1
    zeroProduct = 1

    for value in arr:
        if value != 0:
            product *= value
            zeroProduct *= value

        else:
            product *= value
            zeroProduct *= 1

    
    new_arr = []

    for i in arr:
        if i == 0:
            new_arr.append(zeroProduct)
        else:
            divide = product // i
            new_arr.append(divide)


    return new_arr



    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

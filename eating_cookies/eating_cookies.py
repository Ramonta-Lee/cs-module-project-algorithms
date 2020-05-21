'''
Input: an integer
Returns: an integer
options: eat 1,2,3 at a time
don't know number of cookies

'''
def eating_cookies(n):
    # Your code here
    # n - 1 
    # n - 2 
    # n - 3 

    if n < 0:
        return 0
    
    if n == 0: # return 1 because there is 1 way to not eat any cookies versus to not eat negative cookies
        return 1

    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

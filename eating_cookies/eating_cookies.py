'''
Input: an integer
Returns: an integer
options: eat 1,2,3 at a time
don't know number of cookies

'''
# notation =  O(3^n)
# we are checking 3 ways so it remains constant and then grows exponentially based on the input size
def eating_cookies(n, cache=None): 
    # Your code here
    # n - 1 represents eating 1 cookie
    # eating_cookies(n-1)
    # n - 2 represents eating 2 cookies
    # eating_cookies(n -2)
    # n - 3 represents eating 3 cookies
    # eating_cookies(n-3)
    # want to prevent negative numbers so it doesn't keep going
    if n == 0: # return 1 because there is 1 way to not eat any cookies versus to not eat negative cookies
        return 1

    elif n < 0:
        return 0
    
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = [0 for _ in range(n+1)]
        # we can save our answer to the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

        # by adding them all up it combines to be the total number of ways he can eat cookies
        # this represents our recursive case where there are still some cookies to be eaten
        


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

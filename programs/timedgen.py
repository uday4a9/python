import random
import time


def timed_token(func):
    """
        This is a decorator method to decrorate the original function.
    """
    prev_time = None
    val = None
    def inner():
        """
        This inner method generates the new key for every 3 secs, wiht in 3secs it'll always 
        returns the key which was generated
        """
        nonlocal prev_time, val
        if prev_time == None:
            print("New token generated Freshly")
            prev_time = time.time()
            val = int(random.random() * 100)
            return val
        elif time.time() - prev_time > 3:
            print("New token generated, As old token expired")
            prev_time = time.time()
            val = int(random.random() * 100)
            return val
        else:
            return val
    return inner

@timed_token
def token_gen():
    """
     This acts like aplace eholder method inorder to generate the token
     no effect of return statement
    """
    return "Done with generation"

if __name__ == '__main__':
    for _ in range(18):
        time.sleep(.5)
        print(token_gen())

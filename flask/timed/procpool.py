import multiprocessing
from functools import wraps

def singleton_proc_pool(processes):
    """ 
          This is a prameterized decorator. This method takes 
    the input as number of processes. This argument should be 
    passed as input to create the `multiprocessing.Pool`.
    """
    def get_process_pool(func):
        pool = None
        @wraps(func)
        def create_process_pool():
            nonlocal pool
            if not pool:
                pool = multiprocessing.Pool(processes=processes)
            return pool
        return create_process_pool
    return get_process_pool

@singleton_proc_pool(processes=16)
def funpool():
    """
     This is a placeholder method to imitate singleton pattern.
    Whenever we invoke this method, it returns the same process 
    pool object.
    """
    pass

if __name__ == '__main__':
    p = funpool()

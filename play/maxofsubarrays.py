import queue

# Change this debug to True, print the debug statements
debug = False 

def max_of_sub_arrays(ip, length, slide):
    # A: Creating a deque would be better than list here,
    # R: Rapid(O(1)) insertion and deletions at the ends possible only in deque
    dq = queue.deque()

    # Traverse till slider range and find the greater element index
    for index in range(slide):
        # Till elements exists in dq, the value at the current index in ip
        # is greater than the last index of dq, then pop it from dq.
        ## Conclusion is remove the elements from dq, which are smaller than the
        ## current index.
        while dq and ip[index] >= ip[dq[-1]]:
            debug and print(1, dq)
            dq.pop()
            debug and print(2, dq)

        dq.append(index)

    debug and print(3, dq)

    max_array = []
    # Traverse through the remaining elements in the input
    for index in range(slide, length):
        # Always the first element in dq is the max for the first slider
        # so, do poleft and print it
        oindex = dq[0]
        debug and print("MAX", ip[oindex])
        max_array.append(ip[oindex])
        
        # We got the max value here, so remove the elemnts out of this
        # sliding window
        while dq and dq[0] <= index - slide:
            dq.popleft()

        # Again follow the same logic, what we did to find the max element,
        while dq and ip[index] >= ip[dq[-1]]:
            debug and print(3, dq)
            dq.pop()
            debug and print(3, dq)

        dq.append(index)

    oindex = dq[0]
    max_array.append(ip[oindex])

    debug and print("MAX", ip[oindex])

    print(max_array)


def main():
    # below is the input list ip
    ip = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    ip = [2, 5, -1, 7, -3, -1, -2]

    # subarray size would be 3
    k = 3

    print(ip)
    # need to find max element in each sub-array
    max_of_sub_arrays(ip, len(ip), k)

if __name__ == '__main__':
    main()

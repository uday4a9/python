import sys


def shift_down(heap):
    """
    for index i; childs would be (2 * i + 1) and (2 * i + 2) 
    for any parent i; childs should be lesser weight
        else swap the parent value with max among the childs

    As root always starts from `0`
    """
    parent_ind = 0
    lchild_ind = 1
    rchild_ind = 2

    length = len(heap)

    if not length:
        return

    num = heap[parent_ind]

    while rchild_ind < length:
        # As parent is greateer than the both of the childs
        if num >= heap[rchild_ind] and num >= heap[lchild_ind]:
            break
        # If right child is greater than the left child, Then swap the element with
        # right child
        elif heap[rchild_ind] > heap[lchild_ind]:
            heap[parent_ind] = heap[rchild_ind] 
            parent_ind = rchild_ind
        # if left child is greater than the right child, Then swap element with
        # left child and update the parent index to the same
        else:
            heap[parent_ind] = heap[lchild_ind]
            parent_ind = lchild_ind
        lchild_ind = 2 * parent_ind + 1
        rchild_ind = 2 * parent_ind + 2

    heap[parent_ind] = num


def delete_root_from_heap(heap):
    length = len(heap)
    if not length:
        return

    # As max item index starts from `0`
    length -= 1

    max_item = heap[0]
    heap[0] = heap[length]

    del heap[-1]

    shift_down(heap)
    display(heap)

    return max_item

def shift_up(heap):
    """
    This method needs to invoke only at the time of elemnt insertion -
    - into the heap.
        Property: Element should be greater than the lower level childs
    Complexity : O(log(n)); height of the tree
    """

    last_index = len(heap) - 1
    parent_index = last_index // 2

    temp = heap[last_index]

    while heap[parent_index] < temp and last_index > 0: 
        heap[last_index] = heap[parent_index] 
        last_index = parent_index
        parent_index = last_index // 2

    heap[last_index] = temp


def insert_in_heap(heap):
    """
        While inserting an element to heap, Need to push the element
    at the end of the list, The do restore UP.
    """
    try:
        element = int(input("Enter item to insert:"))
    except ValueError:
        print("Enter integer only")

    heap.append(element)
    shift_up(heap)
    display(heap)

def display(heap):
    print("Heap Contents:", heap)

caller = {0: sys.exit,
          1: insert_in_heap,
          2: display,
          3: delete_root_from_heap
        }

def main():
    heap = []
    while True:
        print("0. exit")
        print("1. insert")
        print("2. display")
        print("3. delete")
        print("")

        try:
            choice = int(input("Enter your choice :"))
        except ValueError:
            print("Enter valid choice")
            continue

        try:
            arg = None if choice == 0 else heap
            caller[choice](arg)
        except KeyError:
            print("Enter correct choice")
            continue


if __name__ == '__main__':
    main()

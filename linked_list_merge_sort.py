from linked_list import LinkedList

def merge_sort(linked_list):
    '''
    Sorts a linked list in ascending order
     - Recursively divide the linked list into siblists containing a single node
     - Repeatedly merge the sublists to produce sublists until one remains

     Returns a sorted linked list
     Takes O(kn logn)
    '''
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    '''
    Divide the unsorted list at mdpoint into sublists
    Takes O(n)
    '''
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    '''
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    '''
    #create a new linked list that containes nodes from merging left and right
    merged = LinkedList()

    #add a fake head that is discarded later
    merged.add(0)

    #set surrent to the head of the linked list
    current = merged.head

    #obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    #iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        #if head node of left is None, we're past the tail
        #add thenode from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            #call next on right to set loop condition to False
            right_head = right_head.next_node
        #if head node of right is None, we're past the tail
        #add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            #call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            #not at either tail node
            #obtain node data to perform comparision operations
            left_data = left_head.data
            right_data = right_head.data
            #if data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                #move left head to next node
                left_head = left_head.next_node
            #if data on left is grater than right, set curent to right node
            else:
                current.next_node = right_head
                #move right head to next node
                right_head = right_head.next_node
        #move current to next node
        current = current.next_node

    #discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
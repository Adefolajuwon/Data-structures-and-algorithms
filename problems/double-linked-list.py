class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_last_node(self):
        itr = self.head
        while itr:
            itr = itr.next
        return

    def print_forward(self):

        if self.head is None:
            print('Empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def print_back(self):
        if self.tail is None:
            print('Empty')
            return
        itr = self.get_last_node()
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

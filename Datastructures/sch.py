class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self, message=''):
        if message:
            print(message)
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        # llstr = ''
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                if itr.next: 
                    itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


if __name__ == '__main__':
    li = LinkedList()
    print('1.Insert values')
    li.insert_values(['banana', 'mango', 'grapes', 'orange'])
    li.print()
    print('2.Insert at beginning')
    li.insert_at_begining('apple')
    li.print()
    print('3.Remove at index')
    li.remove_at(2)
    li.print()
    print('4.Get length:', li.get_length())

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

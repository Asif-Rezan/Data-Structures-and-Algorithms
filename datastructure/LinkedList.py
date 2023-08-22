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

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ''

        while itr:
            listr += str(itr.data) + '==>'
            itr = itr.next

        print(listr)


    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)





if __name__ == '__main__':
    li = LinkedList()
    li.insert_at_begining(5)
    li.insert_at_begining(10)
    li.insert_at_end(15)
    li.insert_at_end(20)
    li.print()

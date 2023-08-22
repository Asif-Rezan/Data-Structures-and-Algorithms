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

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
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


    def remove_at(self,index):
        if index < 0 or self.get_length():
            return Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count +=1

    def insert_at(self,index,data):
        if index < 0 or self.get_length():
            return Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0

        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next

            count += 1




if __name__ == '__main__':
    li = LinkedList()
    li.insert_values(["Asif", "Rezan", "Shahriar"])
    li.remove_at(1)
    li.insert_at(0,"Rezan")
    li.print()

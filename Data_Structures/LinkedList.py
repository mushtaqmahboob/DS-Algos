class Node:

    def __init__(self, info, link=None):
        self.info = info
        self.link = link


class Linkedlist:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, info):

        newnode = Node(info)

        if self.head is None:
            self.head = newnode

        elif self.head is not None:
            newnode.link = self.head
            self.head = newnode

    def insert_at_end(self, info):

        newnode = Node(info)

        if self.head is not None:
            temp = self.head
            while temp.link is not None:
                temp = temp.link
            temp.link = newnode

        elif self.head is None:
            self.head = newnode

    def display(self):

        if self.head is None:
            print('Empty List')

        else:
            temp = self.head
            while temp.link is not None:
                print(temp.info)
                temp = temp.link
            print(temp.info)

ll=Linkedlist()
ll.display()
print('************')
ll.insert_at_beginning(23)
ll.insert_at_end(24)
ll.display()

print('************')

ll.insert_at_end(289)
ll.display()
print('************')

ll.insert_at_beginning(45)
ll.insert_at_end(766)
ll.insert_at_end(249)


ll.display()
print('************')
ll.insert_at_beginning(45)
ll.display()


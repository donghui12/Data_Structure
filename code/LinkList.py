class LinkNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self, node=None):
        self.__headnode = node

    def length(self):
        length = 0
        headnode = self.__headnode
        while headnode:
            headnode = headnode.next
            length += 1

        return length

    def get_all_linklist(self):
        for i in range(1, self.length()+1):
            print(linklist.search(i), "--> ", end="")
        print("None")

    def add(self, data):
        linknode = LinkNode(data)
        linknode.next = self.__headnode
        self.__headnode = linknode

    def append(self, data):
        i = 0
        headnode = self.__headnode
        while i < self.length()-1:
            # print("this is ", i)
            headnode = headnode.next
            i += 1

        linknode = LinkNode(data)
        headnode.next = linknode
        return "OK"

    def insert(self, index, data):
        index = index-1
        if index <= 0:
            self.add(data)
            return "OK"
        elif index > self.length():
            self.append(data)
            return "OK"
        i = 0
        headnode = self.__headnode
        while i < index-1:
            headnode = headnode.next
            i += 1

        linknode = LinkNode(data)
        linknode.next = headnode.next
        headnode.next = linknode
        return "OK"

    def remove(self, index):
        headnode = self.__headnode
        index = index-1
        if index <= 0:
            self.__headnode = headnode.next
            return "OK"
        elif index > self.length():
            index = self.length()-1
        i = 0
        while i < index-1:
            headnode = headnode.next
            i += 1

        temp = headnode.next
        headnode.next = temp.next
        return "OK"

    def change(self, old_index, new_data):
        headnode = self.__headnode
        index = old_index - 1
        if index <= 0:
            headnode.data = new_data
            return "OK"
        elif index > self.length():
            index = self.length() - 1
        i = 0
        while i < index:
            headnode = headnode.next
            i += 1
        headnode.data = new_data
        return "OK"

    def search(self, index):
        if index <= 0 or index > self.length():
            return "Error Index"
        i = 0
        headnode = self.__headnode
        while i < index-1:
            # print("this is ", i)
            headnode = headnode.next
            i += 1

        return headnode.data


if __name__ == "__main__":
    linklist = LinkList()
    linklist.add(3)
    linklist.add(4)
    linklist.get_all_linklist()
    linklist.append(5)
    linklist.append(6)
    linklist.get_all_linklist()
    linklist.change(0, -10)
    linklist.change(13, 11)
    linklist.get_all_linklist()
    linklist.remove(0,)
    linklist.remove(15,)
    linklist.get_all_linklist()
    print(linklist.search(0, ))
    print(linklist.search(1, ))
    print(linklist.search(2, ))
    print(linklist.search(15, ))


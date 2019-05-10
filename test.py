print('hello world')
print("pppppp")
print('1')
print('didi')


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # next为下一节点的内存地址


class Linked_list():
    def __init__(self):
        self.head = None

    def printList(self):
        '''打印所有data'''
        nums = list()
        tmp = self.head
        while tmp:
            nums.append(str(tmp.data))
            tmp = tmp.next
        if len(nums) > 0:
            print('->'.join(nums))

    def insert_to_head(self, data):
        '''链表头部插入'''
        new_node = Node(data)
        if self.head != None:
            new_node.next = self.head
        self.head = new_node  # self.head要始终处于最前方

    def insert_after(self, node, data):
        '''指定节点后面插入'''
        if (not isinstance(node, Node)):
            print('node参数不为Node类')
            return
        if not node or not data:
            print('node或data为空')
            return
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def insert_before(self, node, data):
        '''指定节点前面插入'''
        if (not isinstance(node, Node)):
            print('node参数不为Node类')
            return
        if not node.data or not data:
            print('node或data为空')
            return
        if node == self.head:
            self.insert_to_head(data)
            print('before head插入成功')
            return
        current = self.head
        while current.next and current.next != node:
            current = current.next
        # 循环终止两个情况，第一current.next为空，说明node节点没有找到
        if not current.next:
            print('node不存在')
            return
            # 第二current.next 此时就是 node
        new_node = Node(data)
        new_node.next = node
        current.next = new_node

    def find_by_value(self, data):
        '''根据数值data寻找，返回data所在节点地址'''
        p = self.head()
        while p and p.data != data:
            p = p.next
        if not p:
            print('未找到值为%s的节点' % data)
            return
        return p

    def find_by_index(self, data):
        '''根据数值索引，寻找第data个节点'''
        p = self.head
        position = 0
        while p and position != data:
            p = p.next
            position += 1
        if not p:
            print('索引值%s已超过链表长度' % data)
            return
        return p

    def delete_by_node(self, node):
        '''根据节点删除'''
        current = self.head
        if not isinstance(node, Node):
            print('node参数不为Node类')
            return
        if not current or not node:
            print('链表为空或node为空')
            return
        while current and current.next != node:
            current = current.next
        if not current:
            print('未找到匹配的节点')
            return
        current.next = node.next

    def delete_by_value(self, data):
        '''根据数值删除'''
        current = self.head
        if not current or not data:
            print('链表为空或data为空')
            return
        if self.head.data == data:
            self.head = self.head.next
            print('head已删除')
            return
        while current.next and current.next.data != data:
            current = current.next
        if not current.next:
            print('未找到匹配的data')
            return
        current.next = current.next.next

    def reverse_self(self):
        '''单链表反转'''
        if not self.head or not self.head.next:
            print('链表为空或链表只有一个节点，不用反转')
            return
        node1 = self.head
        node2 = self.head.next
        while node2:
            tmp = node2.next
            node2.next = node1
            node1 = node2
            node2 = tmp
        self.head.next = None
        self.head = node1

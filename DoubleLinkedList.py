'''
双向链表
    只有一个head指针指向头节点
    dll = DoubleLinkedList() 定义一个单链表
              dll.is_empty() 判空                      O(1)
                dll.length() 返回单链表长度             O(n)
                dll.travel() 变量单链表打印所有元素      O(n)
               dll.add(item) 在表头添加元素             O(1)
            dll.append(item) 在队尾添加元素             O(n)
        dll.insert(pos,item) 在指定位置添加元素         O(n)
            dll.remove(item) 删除指定第一个元素         O(n)
            dll.search(item) 查找元素是否存在           O(n)
'''

#定义双向链表节点
class Node:
    def __init__(self,element):
        self.element = element
        self.next = None
        self.prev = None

#定义双向链表
class DoubleLinkedList:

    #默认可以传入一个节点作为单链表的初始节点
    def __init__(self,node=None):
        self.__head = node

    '''判空'''
    def is_empty(self):  
        return self.__head is None

    '''返回列表长度'''
    def length(self):
        if self.is_empty():
            print('链表为空')
        else:
            #用来移动遍历节点
            cur = self.__head
            count = 0
            while cur != None:
                count += 1
                #把下一个节点给cur
                cur = cur.next
            return count

    '''遍历列表打印所有元素'''
    def travel(self): 
        if self.is_empty():
            print('链表为空')
        else:
            #用来移动遍历节点
            cur = self.__head
            while cur != None:
                print(cur.element,end='  ')
                #把下一个节点给cur
                cur = cur.next
            print('')

    '''在表头添加元素'''
    def add(self,item): 
        node = Node(item) 
        if self.is_empty():
            self.__head = node 
        else:
            node.next = self.__head
            self.__head = node
            node.next.prev = node
            # node = self.__head
            # self.__head.prev = node
            # self.__head = node

    '''在表尾添加元素'''
    def append(self,item): 
        #把传入的元素生成结点
        node = Node(item)
        #如果链表为空直接让node等于head
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            #遍历单链表，把尾节点给cur
            while cur.next != None:
                cur = cur.next 
            #把node给尾节点的next
            cur.next = node
            node.prev = cur

    '''在指定位置添加元素'''
    def insert(self,pos,item): 
        '''
        pos = 0 ~ length-1
        '''
        node = Node(item)
        #如果位置小于0默认插入表头
        if pos <= 0 :
            self.add(item)
        #如果插入长度大于等于表长，默认插入表尾
        elif pos >= self.length():
            self.append(item)
        else:
            count = 0
            pre = self.__head
            #遍历单链表，找到pos-1位置的单链表
            while count < (pos - 1):
                count += 1
                pre = pre.next
            #当循环退出后pre指向pos-1，然后修改指向关系，node.next指向pre.next ，pre.next指向node
            node.next = pre.next
            pre.next = node

    '''删除指定元素'''
    def remove(self,item): 
        #cur指针指向删除元素的节点
        cur = self.__head
        while cur != None:
            #特殊情况、1链表为空 2只有一个节点 3删除元素的节点为尾节点
            if cur.element == item:
                #判断是不是头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:  #只有一个节点时cur.next为None
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:  #如果删除的是尾节点
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    '''判断一个元素是否存在'''
    def search(self,item): 
        cur = self.__head
        #遍历链表如果存在return True
        while cur != None:
            if cur.element == item:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    # dll = DoubleLinkedList()
    # print(dll.length())
    # dll.add(3) # 3
    # dll.add(3) # 3 3
    # dll.add(3) # 3 3 3
    # dll.append(6) # 3 3 3 6
    # dll.append(6) # 3 3 3 6 6
    # dll.append(6) # 3 3 3 6 6 6
    # dll.append(6) # 3 3 3 6 6 6 6
    # print(dll.length())
    # dll.add(1) # 1 3 3 3 6 6 6 6
    # dll.append('a') # 1 3 3 3 6 6 6 6 a
    # dll.append('a') # 1 3 3 3 36 6 6 6 a a 
    # dll.append('a') # 1 3 3 3 6 6 6 6 a a a
    # dll.travel()
    # print(dll.length())
    # dll.remove('a')
    # dll.remove(3)
    # dll.remove('a')
    # dll.remove(6)
    # dll.remove('a')
    # dll.add('a')
    # dll.insert(5,'d')
    # print(dll.search('d'))
    # print(dll.search('p'))
    # dll.travel()





   
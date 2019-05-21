'''
单链表方法
    sll = SingleLinkedList() 定义一个单链表
              sll.is_empty() 判空
                sll.length() 返回单链表长度
                sll.travel() 变量单链表打印所有元素
               sll.add(item) 在表头添加元素
            sll.append(item) 在队尾添加元素
        sll.insert(pos,item) 在指定位置添加元素
            sll.remove(item) 删除指定第一个元素
            sll.search(item) 查找元素是否存在
'''

#定义单链表节点
class Node:
    def __init__(self,element):
        self.element = element
        self.next = None

#定义单链表
class SingleLinkedList:

    #默认可以传入一个节点作为单链表的初始节点
    def __init__(self,node=None):
        self.__head = node

    '''判空'''
    def is_empty(self):  
        return self.__head == None

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
        node.next = self.__head
        self.__head = node 

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
    def remove(self,item): # 2 1 2 7 3 4
        #cur指针指向删除元素的节点
        cur = self.__head
        #pre指针指向删除元素的前一节点
        pre = None
        while cur != None:
            #特殊情况、1链表为空 2只有一个节点 3删除元素的节点为尾节点
            if cur.element == item:
                #判断是不是头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                #把cur给pre，cur后移
                pre = cur
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
    sll = SingleLinkedList()
    print('--')
    sll.travel()
    print('--')
    print(sll.is_empty())
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.add(2) # 2 1 2 3 4
    sll.insert(4,7) # 2 1 2 7 3 4
    sll.travel()
    print(sll.is_empty())
    print(sll.length())
    print(sll.search(10))
    sll.append('a') # 2 1 2 7 3 4 a
    print(sll.search('a'))
    sll.remove(2)
    sll.travel()
    sll.remove(7)
    sll.travel()
    sll.remove('a')
    sll.travel()

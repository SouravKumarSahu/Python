# Bi directional link list #

class Node():

    def __init__(self,pre,data,nxt):
        self.pre = pre
        self.data = data
        self.nxt = nxt

    def get_pre(self):
        return self.pre

    def get_data(self):
        return self.data

    def get_nxt(self):
        return self.nxt

    def set_pre(self,pre_node):
        self.pre = pre_node

    def set_data(self,data):
        self.data = data

    def set_nxt(self,nxt_node):
        self.nxt = nxt_node

    def __str__(self):
        return str(self.data)



class LinkList():

    def __init__(self,data):
        self.last_node = Node(None,data,None)
        self.node_count = 1

    def add_node(self,data):
        new_node = Node(self.last_node,data,None)
        self.last_node.set_nxt(new_node)
        self.last_node = new_node
        self.node_count += 1

    def search_node(self,data):
        del_count = 0
        curr_node = self.last_node
        for i in range(self.node_count):
            if curr_node.get_data() == data:
                del_count += 1
                print(f'Found note at position {self.node_count - i}')
                return curr_node
            curr_node = curr_node.get_pre()
        if not del_count:
            print('Node not found')
            return None

    def delete_node(self,data):
        curr_node = self.search_node(data)
        if curr_node:
            pre_node = curr_node.get_pre()
            nxt_node = curr_node.get_nxt()
            pre_node.set_nxt(nxt_node)
            nxt_node.set_pre(pre_node)
            del curr_node
            self.node_count -= 1

    def __str__(self):
        node_list = [hex(id(node)) for node in self.list_node()]
        return str(node_list)

    def __len__(self):
        return self.node_count

    def list_node(self):
        curr_node = self.last_node
        node_list = [curr_node]

        for i in range(1,self.node_count):
            curr_node = curr_node.get_pre()
            node_list.insert(0,curr_node)

        return node_list

###############################################
print("List Creation")
LL1 = LinkList('Sourav')
LL1.add_node('Kumar')
LL1.add_node('Sahu')
LL1.add_node('Dev')
LL1.add_node('Bushan')
LL1.add_node('Tiwari')
LL1.add_node('Ramkrishna')
LL1.add_node('Bhue')

print(f'Print link list LL1 = {LL1}')

print(f'\nLength of link list LL1 = {len(LL1)}')

print('\nBelow are individual data using get_data() method')
for node in LL1.list_node():
    print(node.get_data(),end=' ')

print("\n\nBelow are individual data using __str__() method")
for node in LL1.list_node():
    print(node,end=' ')

print("\n\nSearching data in the link list")
node = LL1.search_node('Kumar')

print(f'\nSearched node = {node}')

print(f'\nPrevious node of the Searched node = {node.get_pre()}')
print(f'\nNext node of the Searched node = {node.get_nxt()}')

        
print('\nDeleting node Sahu')
LL1.delete_node('Sahu')

print(f'\nLength of link list LL1 after delete = {len(LL1)}')

print("\nBelow are individual data using __str__() method")
for node in LL1.list_node():
    print(node,end=' ')

print('\n\nDelete invalid node')
LL1.delete_node('Sam')

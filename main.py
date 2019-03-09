class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def InOrder(T):
    if T is not None:
        InOrder(T.left)
        print(T.item, end = ' ')
        InOrder(T.right)        

def InOrderD(T,space):
    if T is not None:
        InOrderD(T.right,space+'  ')
        print(space,T.item)
        InOrderD(T.left,space+'  ')

def search(T, k):
    while T != None and T.item != k:
        if T.item > k:
            T = T.left
        elif T.item < k:
            T = T.right
    return T

def BBST(T,k):
    if not k:
        return None
    mid = len(k)//2
    root = BST(k[mid])
    root.left = BBST(T,k[:mid])
    root.right = BBST(T,k[mid+1:])
    return root

def Extracting (T, length):
    E = []
    E.append(T)
    for i in range(length):
        temp = E[i]
        if temp.left:
            E.append(temp.left)
        if temp.right:
            E.append(temp.right)
    return E

def OrderedByDepth(T,k):
    if T == None:
        return
    if k == 0:
        print(T.item)
    else:
        OrderedByDepth(T.left,k-1)
        OrderedByDepth(T.right,k-1)
    

T = None
B = [10,4,15,2,8,1,3,5,9,7,12,18]
length = len(B)
for a in B:
    T = Insert(T,a)
    
InOrderD(T,'')
print(search(T, 5))
print('  ')
print('  ')
print('  ')
S = BBST(T,B)
InOrderD(S,'')
print('  ')
print('  ')
print('  ')
E = Extracting (T,length)
for i in range(length):
    print(E[i].item)
print('  ')
print('  ')
print('  ')
print(OrderedByDepth(T,3))

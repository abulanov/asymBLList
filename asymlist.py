class TransitionBackError(Exception):
    def __init__(self, message):
        self.message = message

class Node:
    def __init__(self, node_id, is_bidirect, **kwargs):
        ''' Used by AsymLList. Not instantiated directly
        
            Parameters:

            node_id: unique Node id
            is_bidirect (boolean): flags if the Node can be traversed in forward 
            and reverse direction (True) or only in forward direction (False) 
                 
        '''
        self.id=node_id
        self.is_bidirect=is_bidirect

        # self.prev - pointer to the previous bidirectional Node 
        # self.next - pointer to the next Node
        self.prev=None
        self.next=None
        

    def __str__(self):
        return str(self.id)    
        
    def __repr__(self):
        return "Node:{} Prev:{} Next:{}".format(self.id,self.prev,self.next)

class AsymLList:
    def __init__(self,node_id, is_bidirect=True, nodeClass=Node, **kwargs):
        '''Instantiates AsymLList with the first Node

           parameters:

           node_id, is_bidirect:  Node class attrributes.
           nodeClass: class of the Node        
        '''
        self.nodeClass=nodeClass
        firstNode=self.nodeClass(node_id,is_bidirect, **kwargs)
        
        if firstNode.is_bidirect: 
            self.back=firstNode
        else:
            self.back=None    
        # self.begin - pointer to the first Node of the AsymList
        # self.last - pointer to the last Node of the AsymLyst
        # self.current - pointer to the Node under consideration. 
        #                used in fwd() and rwd() methods          
        self.begin=firstNode 
        self.last=firstNode
        self.current=None
        
    def append(self,node_id,is_bidirect=True, **kwargs):
        ''' Appends a Node to the AsymLList.

            Parameters: 
                node_id: unique node id
                is_biderect (boolean): is node biderectional, default - True

            Reurns the pointer to the last node.
        '''
        newNode = self.nodeClass(node_id,is_bidirect, **kwargs)
        newNode.prev = self.back 
        self.last.next = newNode  
        if newNode.is_bidirect:
            self.back = newNode
        self.last = newNode   
        return self.last
        
    def forward(self):
        ''' Returns a list of Nodes linked in the forward direction
            starting from the first one
        '''
        result = []
        ptr = self.begin
        while ptr is not None:
            result.append(ptr)
            ptr = ptr.next
        return result    
    
    def backward(self):
        ''' Returns a list of Nodes linked in the backward direction,
            strting from the last bidirectional Node, or None if the 
            list is empty.
        '''
        if self.back is None:
            return None
        result = []
        ptr = self.back
        while ptr is not None:
            result.append(ptr)
            ptr = ptr.prev
        return result    
            
    def fwd(self):
        '''Traverses throgh the Nodes of the AsymLList in forward direction.
           Returns the pointer to the next Node. when self.current points to the last Node,
           turns over to the first Node 
        '''
        if self.current is None:
            self.current=self.begin
        else: 
            self.current=self.current.next
            if self.current is None:
                self.current=self.begin
        return self.current
    
    def rwd(self):
        '''Traverses through the Nodes of the AsymLList in the reverse direction.
           Returns the pointer to the previous Node if exists, otherwise raises an Exeption.
           When self.current points to the first biderectional Node, turns over to 
           the last bidirectional Node.   
        '''
        if self.back is None:
            raise TransitionBackError("No way back")
        if self.current is None:
            self.current = self.back
        else: 
            self.current = self.current.prev
            if self.current is None:
                self.current = self.back
        return self.current


class OidNode(object):
    """
    A class which represents a node in the OID tree
    """
    def __init__(self, oid, name):
        """
        When created an OID node must have an oid string such as
        '2' or '2.4.6.1.20.3' which when concatinated with its parent
        creates the absolute OID.
        
        If no parent is supplied this nodes OID is assumed to be absolute
        """
        self.oid = oid
        self.name = name
        self.parent = None
        self.children = {}
    
    def absolute_oid(self):
        return '%s.%s' % (self.parent, self.oid) if self.parent is not None else str(self.oid)
    
    def __str__(self):
        """
        When determining the absolute OID for a particular node,
        it is constructed by concatinating its own OID on to the
        end of its parents absolute OID.
        """
        return self.absolute_oid()
    
    def addChild(self, node):
        """
        Adds a node to the dictionary of child nodes under this node,
        which regard this node as their parent
        """
        self.children[node.name] = node
        node.parent = self
    
    def addChildren(self, nodes):
        for node in nodes:
            self.addChild(node)
    
    def getChildren(self):
        return self.children
            
    def __getitem__(self, name):
        return self.children[name]
    
    def __setitem__(self, name, oid):
        self.children[name] = OidNode(oid, name)
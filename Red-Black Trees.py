# defining the structure of node of the red-black tree
class RBNode():
  def __init__(self,val):
    self.val = val
    self.parent = None
    self.left = None
    self.right = None
    self.color = 1            # '1' represents the color of node is red and '0' black


# creating class called RBTree where all the operations are defined
class RBTree():
  def __init__(self):
    self.NULL = RBNode(0)
    self.NULL.color = 0
    self.NULL.left = None
    self.NULL.right = None
    self.root = self.NULL


  def insert(self, val):
    new_node = RBNode(val)
    new_node.parent = None
    new_node.left = self.NULL
    new_node.right = self.NULL
    new_node.color = 1

    root = None
    curr_node = self.root

    # to traverse till the required the position
    while curr_node != self.NULL:
      root = curr_node
      if new_node.val < curr_node.val:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right


    # inserting node at the required position
    new_node.parent = root
    if root == None:
      self.root = new_node
    elif new_node.val < root.val:
      root.left = new_node
    else:
      root.right = new_node

    if new_node.parent == None:
      new_node.color = 0
      return

    if new_node.parent.parent == None:
      return

    # to remove the violations of red-black tree
    self.remove_violations(new_node)


  # function to remove violations
  def remove_violations(self,new_node):
    while new_node.parent.color == 1 and new_node != self.root:

      if new_node.parent == new_node.parent.parent.right:
        uncle = new_node.parent.parent.left
        if uncle.color == 1:
          new_node.parent.color = 0           #changing the color of new node's parent
          uncle.color = 0                     #changing the color of new node's uncle
          new_node.parent.parent.color = 1    #changing the color of new node's grandparent
          new_node = new_node.parent.parent   #setting grandparent node as the new node to check for further violations
        else:
          if new_node == new_node.parent.left:
            new_node = new_node.parent
            self.rotate_right(new_node)
          new_node.parent.color = 0
          new_node.parent.parent.color = 1
          self.rotate_left(new_node.parent.parent)

      else:
        uncle = new_node.parent.parent.right
        if uncle.color == 1:
          new_node.parent.color = 0           #changing the color of new node's parent
          uncle.color = 0                     #changing the color of new node's uncle
          new_node.parent.parent.color = 1    #changing the color of new node's grandparent
          new_node = new_node.parent.parent   #setting grandparent node as the new node to check for further violations
        else:
          if new_node == new_node.parent.right:
            new_node = new_node.parent
            self.rotate_left(new_node)
          new_node.parent.color = 0
          new_node.parent.parent.color = 1
          self.rotate_right(new_node.parent.parent)

      if new_node == self.root:
        break
    
    self.root.color = 0


  # function to implement left rotation
  def rotate_left(self, x):
    y = x.right
    x.right = y.left
    if y.left != self.nil:
      y.left.parent = x

    y.parent = x.parent
    if x.parent == None:
      self.root = y
    elif x == x.parent.left:
      x.parent.left = y
    else:
      x.parent.right = y
    y.left = x
    x.parent = y


  # function to implement right rotation
  def rotate_right(self, x):
    y = x.left
    x.left = y.right
    if y.right != self.nil:
      y.right.parent = x

    y.parent = x.parent
    if x.parent == None:
      self.root = y
    elif x == x.parent.right:
      x.parent.right = y
    else:
      x.parent.left = y
    y.right = x
    x.parent = y

  
  # function to print the resultant red-black tree
  def __print( self , node , indent , last ):
    if node != self.NULL :
      print(indent, end=' ')
      if last:
        print ("R---->",end= ' ')
        indent += "     "
      else :
        print("L---->",end=' ')
        indent += "|    "

      node_color = "RED" if node.color == 1 else "BLACK"
      print ( str ( node.val ) + "(" + node_color + ")" )
      self.__print( node.left , indent , False )
      self.__print( node.right , indent , True )

    # Function to call print
  def print_tree ( self ) :
    self.__print( self.root , "" , True )



if __name__ == "__main__":
  # list of tasks 
  tasks = [27, 19, 34, 7, 25, 2, 31, 65, 49, 98]

  # creating object named tree of the class RBTree 
  tree = RBTree()

  for i in range(len(tasks)):
    tree.insert(tasks[i])
    print("\n")
    print(f"STEP {i+1} :  ")
    tree.print_tree()
    print("\n")





    

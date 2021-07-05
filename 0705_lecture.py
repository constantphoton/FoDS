# binary search trees -search

class BST():
    def __searchHelp(curNode:TreeNode,x)->TreeNode:#user can't recognize searchHelp func
    #user only uses search function

        if not curNode:
            return None
        if x == curNode.val:
            return curNode
        elif x<curNode.val:
            return self.__searchHelp(curNode.left,x)
        else:
            return self.__searchHelp(curNode.right,x)

    def search(self,x:int) ->TreeNode:
        return self.__searchHelp(self.root,x)
    



        

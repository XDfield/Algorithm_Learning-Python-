'''二叉树的前序遍历,中序遍历,后序遍历'''


class Node:
    '''
    二叉树的节点类
    '''

    def __init__(self, data, left, right):
        self.data = data
        self._left = left
        self._right = right


class BinaryTree:
    '''
    二叉树类
    '''

    def __init__(self, node=None):
        '''初始化一个二叉树'''
        self._root = node

    def make_tree(self, node):
        '''构造二叉树'''
        self._root = node

    def pre_order(self):
        '''前序遍历'''
        result = list()

        def order(node):
            result.append(node.data)
            if node._left:
                order(node._left)
            if node._right:
                order(node._right)
        order(self._root)
        return result

    def in_order(self):
        '''中序遍历'''
        result = list()

        def order(node):
            if node._left:
                order(node._left)
            result.append(node.data)
            if node._right:
                order(node._right)
        order(self._root)
        return result

    def post_order(self):
        '''后序遍历'''
        result = list()

        def order(node):
            if node._left:
                order(node._left)
            if node._right:
                order(node._right)
            result.append(node.data)
        order(self._root)
        return result


def main():
    node1 = Node(1, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(3, node1, node2)
    node4 = Node(4, 0, 0)
    node5 = Node(5, node4, node3)

    tree = BinaryTree(node5)
    print('前序遍历: ' + str(tree.pre_order()))
    print('中序遍历: ' + str(tree.in_order()))
    print('后序遍历: ' + str(tree.post_order()))


if __name__ == '__main__':
    main()

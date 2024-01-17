from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""Получить 2 дерева, обойти оба. В результате обхода добавить листовые значения в 2 списка. 
В результате, вернуть bool: равны ли листья у данных деревьев?"""


# 1-й способ, рекурсия
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Инициализация двух списков для хранения листьев двух деревьев
        first_tree_leafs = []
        second_tree_leafs = []

        # Обход первого дерева и добавление листьев в список first_tree_leafs
        self.traverse(root1, first_tree_leafs)
        # Обход второго дерева и добавление листьев в список second_tree_leafs
        self.traverse(root2, second_tree_leafs)

        # Возвращение результата сравнения списков листьев двух деревьев
        return first_tree_leafs == second_tree_leafs

    def traverse(self, node, leafs):
        # Если текущий узел None, завершаем обход
        if not node:
            return

        # Если текущий узел - лист, добавляем его значение в список leafs
        if not node.left and not node.right:
            leafs.append(node.val)
            return

        # Рекурсивный обход левого поддерева, если оно существует
        if node.left:
            self.traverse(node.left, leafs)
        # Рекурсивный обход правого поддерева, если оно существует
        if node.right:
            self.traverse(node.right, leafs)


# 2-й способ, итеративный
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Инициализация стеков для обхода деревьев и списка для хранения пар листьев
        stack1: List[TreeNode] = [root1]
        stack2: List[TreeNode] = [root2]
        # Инициализация активного стека для текущего обхода
        active_stack = stack1
        leaf_pair: List[int] = []  # Список для хранения пары листьев

        while stack1 or stack2:
            if not active_stack:
                return False
            # Извлечение узла из активного стека
            root: TreeNode = active_stack.pop()
            # Добавление правого и левого потомка в стек, если они существуют
            if root.right:
                active_stack.append(root.right)
            if root.left:
                active_stack.append(root.left)
            # Если узел - лист, добавляем его значение в leaf_pair
            if not root.left and not root.right:
                leaf_pair.append(root.val)
                if len(leaf_pair) == 1:
                    active_stack = stack2
                elif len(leaf_pair) == 2:
                    # При достижении двух листьев в паре, проверяем их равенство
                    if leaf_pair[0] != leaf_pair[1]:
                        return False
                    active_stack = stack1
                    leaf_pair.clear()

        # Проверка, что все листья обоих деревьев были сравнены
        return len(leaf_pair) == 0

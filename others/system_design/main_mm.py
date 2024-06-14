# # [3,9,20,null,null,15,7]
# # # 3
# # 9 20
# #    15 7

# class Node:
#     def __init__(self,val = 0, left=None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

# def maxDepth(root):
#     if not root:
#         return 0
#     left_side = maxDepth(root.left)
#     right_side = maxDepth(root.right)
#     return max(left_side, right_side) + 1


# root = Node(3)
# root.left = Node(9)
# root.right = Node(20)
# root.right.left = Node(15)
# root.right.right = Node(7)

# print(maxDepth(root))


# abc

# a b c

# abbaccabd = set()
# ababcbaba

# len 

# []

# ["a", "b"]

# O(n)

# sort(reverse=True)















# for i in len(string)

#     rec_func(i)    


def palindrome(s):
    
    def check(left,right):
        while s[left] == s[right] and left >= 0 and right < len(s):
            o.append(s[left:right+1])
            left -= 1
            right += 1

    o = []
    for i in range(len(s)):
        
        check(i,i)
        check(i,i + 1)

    return o



s = "acbbccabd"

1 
3
5
7
9
7
5
3
1


print(palindrome(s))

# a b c d ababa bb cc acca 



















import sys

N = int(sys.stdin.readline())
global idx
idx = -1

def make_tree(post_ord, tree_dict):
  stack = []
  for node in post_ord:
    #print(stack)
    if node == 'nil':
      stack.append(node)
    else:
      tree_dict[node] = ['','']
      tree_dict[node][1] = stack.pop()
      tree_dict[node][0] = stack.pop()
      stack.append(node)


for _ in range(N):
  A_input = list(sys.stdin.readline().split())
  B_input = list(sys.stdin.readline().split())
  A_input.pop()
  B_input.pop()
  A_tree = {}
  B_tree = {}
  make_tree(A_input, A_tree)
  #print(A_tree)
  make_tree(B_input, B_tree)
  #print(B_tree)
  if tuple(sorted(A_tree.keys())) != tuple(sorted(B_tree.keys())):
    print('false')
  else:
    answer = 'true'
    for key in A_tree.keys():
      if set(A_tree[key]) != set(B_tree[key]):
        answer = 'false'
    print(answer)
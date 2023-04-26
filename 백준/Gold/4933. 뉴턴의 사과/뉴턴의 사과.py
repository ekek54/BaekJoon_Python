import sys

N = int(sys.stdin.readline())
global idx
idx = -1

def make_tree(tree_post_ord, tree_dict):
  global idx
  cur_node = tree_post_ord[idx]
  if cur_node == 'nil':
    return
  if not cur_node in tree_dict:
    tree_dict[cur_node] = ['nil', 'nil']
  idx -= 1
  #print(idx)
  tree_dict[cur_node][1] = tree_post_ord[idx]
  make_tree(tree_post_ord, tree_dict)
  idx -= 1
  tree_dict[cur_node][0] = tree_post_ord[idx]
  make_tree(tree_post_ord, tree_dict)
  return


for _ in range(N):
  A_input = list(sys.stdin.readline().split())
  B_input = list(sys.stdin.readline().split())
  A_input.pop()
  B_input.pop()
  A_tree = {}
  B_tree = {}
  idx = -1
  make_tree(A_input, A_tree)
  #print(A_tree)
  idx = -1
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
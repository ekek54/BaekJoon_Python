import sys
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())
nodes = [(-1, -1) for _ in range(N)]
for _ in range(N):
    a, b, c = map(lambda x: int(x) - 1,sys.stdin.readline().split())
    nodes[a] = (b, c)

def last_node(node):
    if nodes[node][1] == -2:
        return node
    return last_node(nodes[node][1])

visit_cnt = 0
answer = 0
last = last_node(0)
#print(last)
def pseudo_inorder(node_num):
    global answer
    global visit_cnt
    answer += 1
    #print(node_num)
    visit_cnt += 1
    if (nodes[node_num][0] != -2):
        if not pseudo_inorder(nodes[node_num][0]):
            #print(node_num)
            answer += 1
        else: return True
    if (nodes[node_num][1] != -2):
        if not pseudo_inorder(nodes[node_num][1]):
            #print(node_num)
            answer += 1
        else: return True
    if node_num == last and visit_cnt == N: return True
    return False
pseudo_inorder(0)
print(answer - 1)
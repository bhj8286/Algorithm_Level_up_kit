# 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 변수
memory = []
root = None
current = None
nameAry = ['블랙핑크', '레드벨벳', '에이핑크', '걸스데이', '트와이스', '마마무']

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node) # 안중요!

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name

    current = root

    while True: # while True: 루프 내부에서 조건을 만족할 때까지 계속 반복됩니다.
        if (name < current.data):
            if (current.left == None):
                current.left = node
                break
            current = current.left
        else:
            if (current.right == None):
                current.right = node
                break
            current = current.right

    memory.append(node)

print('이진 탐색 트리 완료!')

findname = '바바부'
current = root 
while True:
    if (findname == current.data):
        print(findname, '찾았다')
        pass
        break
    elif (findname < current.data):
        if (current.left != None):
            print(findname, '없음')
            break
        current = current.left
        
    else:
        if (current.right != None):
            print(findname, '없음')
            break
        current = current.right

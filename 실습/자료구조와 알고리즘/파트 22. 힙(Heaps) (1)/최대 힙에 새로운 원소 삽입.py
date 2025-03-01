class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        idx = len(self.data) - 1
        ### idx가 1 = 루트노드 
        while idx > 1 :
            if self.data[idx] > self.data[idx//2]:
                self.data[idx],self.data[idx//2] = self.data[idx//2], self.data[idx]
                idx = idx//2
            else:
                break
                


def solution(x):
    return 0
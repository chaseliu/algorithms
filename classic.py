"""Classic Algorithms"""

def hanoi(n):
    """HanoiTower with n disks"""
    steps = []

    def _move(disk, src, dst):
        """Move disk from src to dst"""
        steps.append(f"Move disk {disk} from {src} to {dst}")

    def _hanoi(n, src, aux, dst):
        """
        Hanoi recursive unit
        Solve problem: Move n disks from src to dst via aux.
        It can be divided into 3 steps:
        Step 1: Solve sub problem: Move n - 1 disks from src to aux via dst as aux
        Step 2: Move the nth disk from src to dst
        Step 3: Solve sub problem: Move n - 1 disks from aux to dst via src as aux
        """
        if n == 1:
            _move(n, src, dst)
        else:
            _hanoi(n - 1, src, dst, aux)
            _move(n, src, dst)
            _hanoi(n - 1, aux, src, dst)

    _hanoi(n, 'A', 'B', 'C')
    return steps


def longest_mountain(A) -> int:
    ans = i = j = 0
    n = len(A)
    while i + 2 < n:
        j = i + 1
        # 判断当前i位置是否符合左侧山脚
        if A[i] < A[i + 1]:
            # 将j移至山峰
            while j < n - 1 and A[j] < A[j + 1]:
                j += 1
            # 判断当前j位置是否符合右侧山坡起点
            if j < n - 1 and A[j] > A[j + 1]:
                # 移动j至右侧山脚
                while j < n - 1 and A[j] > A[j + 1]:
                    j += 1
                # 保存最大长度
                ans = max(ans, j - i + 1)
            # 如不符合，有两种情况：
            # 1. 山峰已经是数组最后一个元素，应该返回结果
            # 2. 山峰出现两个相同的值，应该将i跳至j+1
            # 第一种情况也可以通过j递增1后赋值给i然后退出循环来实现
            else:
                j += 1
        # 右侧山脚可能是下一个左侧山脚
        i = j
    return ans

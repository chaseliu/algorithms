"""String related algorithms"""
from typing import List
import time

def partitionLabels(S: str) -> List[int]:
    d = {s: i for i, s in enumerate(S)}
    res, start, end = [], 0, 0
    for i, s in enumerate(S):
        end = max(end, d[s])
        if i == end:
            res.append(end - start + 1)
            start = end + 1
    return res




if __name__ == "__main__":
    res = partitionLabels("ababcbacadefegdehijhklij")
    print(res)

from typing import List

def ninjaAndRegularPolygon(n: int, m: int, a: List[int]) -> str:
    return "YES" if a.count(max(a)) >= m else "NO"

# Example usage
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(ninjaAndRegularPolygon(n, m, a))

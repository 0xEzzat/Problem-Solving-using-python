n, h = map(int, input().split())
heights = list(map(int, input().split()))
ans = n
for val in heights:
    ans += val > h

print(ans)
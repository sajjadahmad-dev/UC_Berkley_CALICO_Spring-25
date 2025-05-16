def solve_ben_in_middle(N):
    return 'u' + 'wu' * N
T = int(input())
for _ in range(T):
    N = int(input())
    print(solve_ben_in_middle(N))
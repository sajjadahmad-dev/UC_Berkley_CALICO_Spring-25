num_cases = int(input())

for _ in range(num_cases):
    s = input().strip()
    u_indices = [i for i, char in enumerate(s) if char == 'u']
    total_pairs = 0
    n = len(u_indices)
    
    prefix_w = [0] * (len(s) + 1)
    for i in range(len(s)):
        prefix_w[i+1] = prefix_w[i] + (1 if s[i] == 'w' else 0)
    
    for i in range(n):
        for j in range(i + 1, n):
            u1 = u_indices[i]
            u2 = u_indices[j]
            if prefix_w[u2] - prefix_w[u1 + 1] > 0:
                total_pairs += 1
    print(total_pairs)
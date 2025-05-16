num_tests = int(input())

for _ in range(num_tests):
    text = input().strip()
    text_length = len(text)
    
    w_counts = [0] * (text_length + 1) 
    for i in range(text_length):
        if text[i] == 'w':
            w_counts[i + 1] = w_counts[i] + 1
        else:
            w_counts[i + 1] = w_counts[i]

    u_places = [] 
     
    for i in range(text_length):
        if text[i] == 'u':
            u_places.append(i)
        pair_count = 0

    num_us = len(u_places)
    for i in range(num_us):
        for j in range(i + 1, num_us):
            first_u = u_places[i]
            second_u = u_places[j]
            if first_u < second_u:
                w_between = w_counts[second_u] - w_counts[first_u + 1]  
                if w_between > 0:
                    pair_count += 1
    print(pair_count)
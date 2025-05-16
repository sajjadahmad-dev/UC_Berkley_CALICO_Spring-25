def compute_total_expense(scenarios):
    doubledouble = 2  
    payouts = []
    
    for people_count, decisions in scenarios:
        offer = 1
        expense = 0
        
    
        for action in decisions:
            if action == 'T':
                expense += offer  
                offer = 1         
            else:  # action == 'D'
                offer = offer * doubledouble 
        
        payouts.append(expense)
    
    return payouts

num_scenarios = int(input())
case_data = []

while len(case_data) < num_scenarios:
    count = int(input())
    sequence = input().strip()
    case_data.append((count, sequence))

for payout in compute_total_expense(case_data):
    print(payout)
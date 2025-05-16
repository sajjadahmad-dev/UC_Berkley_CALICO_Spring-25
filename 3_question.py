def find_tournament_winner():

    num_tests = int(input())

    for _ in range(num_tests):
  
        num_players = int(input())
        

        player_names = input().split()
        player_powers = list(map(int, input().split()))
        

        current_names = player_names.copy()
        current_powers = player_powers.copy()
        

        while len(current_names) > 1:
            new_names = []
            new_powers = []

            for i in range(0, len(current_names), 2):
                name1 = current_names[i]
                power1 = current_powers[i]
                name2 = current_names[i + 1]
                power2 = current_powers[i + 1]
                

                if power1 > power2:
                    winner_name = name1
                    winner_power = power1 + power2
                elif power2 > power1:
                    winner_name = name2
                    winner_power = power1 + power2
                else:
       
                    winner_name = name1 + name2
                    winner_power = power1 + power2
                
                new_names.append(winner_name)
                new_powers.append(winner_power)
            
   
            current_names = new_names
            current_powers = new_powers
        
  
        champion = current_names[0]
        print(champion)


find_tournament_winner()
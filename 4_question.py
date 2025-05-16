def count_button_moves():
    num_tests = int(input())
    for _ in range(num_tests):
        rows, cols = map(int, input().split())

        grid = []
        for _ in range(rows):
            row = list(map(int, input().split()))
            grid.append(row)

        button_rows = {}  
        button_cols = {}  
        for r in range(rows):
            for c in range(cols):
                button_num = grid[r][c]
                button_rows[button_num] = r
                button_cols[button_num] = c
        
   
        current_row = 0
        current_col = 0
        moves_needed = 0

        for button in range(1, rows * cols + 1):
            target_row = button_rows[button]
            target_col = button_cols[button]
  
            row_diff = abs(current_row - target_row)
            vertical_moves = min(row_diff, rows - row_diff)
            
            col_diff = abs(current_col - target_col)
            horizontal_moves = min(col_diff, cols - col_diff)
            
            
            moves_needed += vertical_moves + horizontal_moves
            
        
            current_row = target_row
            current_col = target_col
        
     
        print(moves_needed)

count_button_moves()
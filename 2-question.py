def get_rectangle_area():
  
    num_tests = int(input())
    
    for _ in range(num_tests):
        num_points = int(input())
        
        points_x = []
        points_y = []
        
        for _ in range(num_points):
            x, y = map(float, input().split())
            points_x.append(x)
            points_y.append(y)
    
        smallest_x = min(points_x)  
        biggest_x = max(points_x)   
        smallest_y = min(points_y)  
        biggest_y = max(points_y)   
        

        rectangle_width = biggest_x - smallest_x
        rectangle_height = biggest_y - smallest_y
        
 
        rectangle_area = rectangle_width * rectangle_height
        
 
        print(rectangle_area)


get_rectangle_area()
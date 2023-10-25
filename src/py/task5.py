def check_character_status(coordinates):
    enemies = set() 
    
    for coordinate in coordinates:
        if coordinate in enemies:
            print("The character died")
            return
        
        for i in range(coordinate[0]-1, coordinate[0]+2):
            for j in range(coordinate[1]-1, coordinate[1]+2):
                new_enemy = (i, j)
                enemies.add(new_enemy)
    
    print("The character survived")

N = int(input("Enter the number of coordinates: "))

coordinates = []
for i in range(N):
    x, y = map(int, input("Enter the x and y coordinates separated by space: ").split())
    coordinates.append((x, y))

check_character_status(coordinates)

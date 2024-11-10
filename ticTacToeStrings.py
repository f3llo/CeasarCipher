import os
def print_field(field): 
    os.system("clear")
    for i in range(0, len(field), 3): print(field[i], field[i+1], field[i+2], "\n");
def check_win(field): #probably the most elegant solution I can find -> better than if statements 
    line = ''.join(field)
    win_conditions = [line[0:3], line[3:6], line[6:9], line[0::3], line[1::3], line[2::3], line[0] + line[4] + line[8], line[2] + line[4] + line[6]]
    return any(winner in ['XXX', 'OOO'] for winner in win_conditions)
def place_field(field, i, t): #add mechanic that if you miss you place randomly
    field[i] = t if field[i] == "0" else place_field(field, int(input(f"Enter move position ({t}): ")), t, counter)
    print_field(field)
counter, win, field = 0, False, ["0"] * 9
print_field(field)
print("\n Place values by index. Positions indexed 1-9 where top left is 1 and bottom right is 9.")
while check_win(field) == False:
    place_field(field, int(input("Enter move position (X): "))-1, "X"); counter += 1
    if check_win(field) == True or counter == 9: break
    place_field(field, int(input("Enter move position (O): "))-1, "O"); counter += 1
print("Tie") if counter == 9 else print("You Won!")

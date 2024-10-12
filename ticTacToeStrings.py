import os
def print_field(field): 
    os.system("cls")
    for i in range(0, len(field), 3): print(field[i], field[i+1], field[i+2], "\n")

def check_win(field): #not the most elegant solution PEP 8 violation
    if (field[0] == field[4] == field[8] or field[2] == field[4] == field[6]) and field[4] != "0": return True
    if (field[0] == field[1] == field[2] or field[3] == field[4] == field[5] or field[6] == field[7] == field[8]) and field[0] != "0" or field[3] != "0" or field[6] != "0": return True
    if (field[0] == field[3] == field[6] or field[1] == field[4] == field[7] or field[2] == field[5] == field[8]) and field[0] != "0" or field[1] != "0" or field[2] != "0": return True
    return False

def place_field(field, i, t):
    field[i] = t if field[i] == "0" or field[i] == "X" or field[i] == "O" else print("Non-Zero field: already occupied!")
    print_field(field)
    return check_win(field)

field, win = ["0"] * 9, False
print(print_field(field), "\n", "Place values by entering an index. Positions are indexed 1-9 where top left is 1 and bottom right is 9.")
while win != True:
    win = place_field(field, int(input("Enter move position (X): "))+1, "X")
    win = place_field(field, int(input("Enter move position (O): "))+1, "O")
print("You Won!")
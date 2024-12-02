a = [[None]*3]*3
a2 = [[i+j for i in range(0,5)] for j in range(0,13,4)]

for i in range (0, len(a)):
    for j in range (0, len(a)):
        print(a[i][j])

#find sum of horizontals or verticals
total = 0
rowNum = 0
for i in range (0, len(a)):
    total += a[rowNum][i]
    #total += a[i][rowNum] -> horizontals

#find sum of matrix diagonals

for i in range (0, len(a)):
    total += a[i][i]
    #total += a[i][3-i]

loop I from 0 to N
    students[I][4] = students[I][1]*0.3 + students[I][2]*0.3 + students[I][3]*0.4
end loop

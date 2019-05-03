x = input("Enter a string: ")
y = input("Enter a pattern: ")

m = len(x)
n = len(y)
result = ''
temp = 'Null'
j = 0
i = 0

for i in range(len(x)):

    if j > n - 1:
        break

    if y[j] == '.':

        if temp == 'NULL':
            result += temp
            break
        else:
            result += x[i]
            j = j + 1
            i = i + 1
        if i != m:
            temp = x[i]
            
    elif y[j] == '*':        
        if i == 0 or temp == 'Null':
            j = j + 1
            break
        
        if  i != m + 1:
            if temp == x[i]:
                result += x[i]
                i = i + 1
            else:
                temp = x[i]
                result += x[i]
                j = j + 1
                
    elif i < m + 1:
        temp = x[i]
        result += x[i]
        j = j + 1
        i = i + 1
    else:
        break

if x == result:
    print('True')
else:
    print('False')
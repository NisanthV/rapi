def matrix_dianogol(auto_gnerate):
    row = []
    col = []
    if type(auto_gnerate)=='str':
        auto_gnerate=auto_gnerate.lower()

    if auto_gnerate==1 or auto_gnerate=='yes':
        for i in range(0, 100):
            col.append(i)
    else:
        for i in range(0,10):
            for j in range(0,10):
                col=input(f'row {i}  value of coloumn {j} your value:')

    for i in range(0, 10):
        print('\n')
        row.append(col[i])
        for j in range(0, 10):
            print(col[j], "\t", end='')
    temp=0
    for i in row:
        temp=row[i]+temp
    return temp

def remove_vowels():
    vowels=['a','e','i','o','u']
    string=input("enter the string").lower()
    lis=[]
    for i in range(len(string)):
        if string[i] in vowels:
            continue
        else:
            lis.append(string[i])

    return "".join(lis)

def check_parathesis():
    left,right=0,0
    string=input('enter string')
    for i in range(len(string)):
        if string[i]=='(':
            left+=1
            continue
        elif string[i]==')':
            right+=1
            continue
        else:
            continue

    if left==right:
        return 0
    else:
        return 1
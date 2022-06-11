import random
import os

def is_bomb(list1, list2, a, b):
    # returns true if a bomb is at coordinates (a,b)
    for index , val in enumerate(list1):
        if val==a:
            if list2[index]==b:
                return True
    return False

def in_game(ligne, colonne, x,y):
    # check if coordinates (x,y) are not out of range
    if x<0 or x>=ligne or y<0 or y>=colonne:
        return False
    return True

def check_case(list1, list2, a, b):
    # returns the number of bombs around coordinates (a,b) or # if a bomb is there
    x=a-1
    y=b-1
    number_of_bomb=0
    if is_bomb(list1, list2, a, b):
        return '#'
    else:
        for i in range(x, x+3):
            for j in range(y, y+3):
                if in_game(ligne, colonne, i, j):
                    if i==a and j==b:
                        pass
                    else:
                        for index, val in enumerate(list1):
                            if val == i:
                                if list2[index]==j:
                                    number_of_bomb+=1
    return number_of_bomb

def is_null(a):
    return a==0

def insert_null_tab_user(tab_user, tab_response, i , j):
    # update 'tab_user' according to entered coordinates (i,j)
    # if the square is empty, finds and reveals the empty squares around
    if in_game(ligne, colonne, i, j):
        if tab_user[i][j]=='o':
            x=i-1
            y=j-1
            for k in range(x,x+3):
                for l in range(y,y+3):
                    if is_null(tab_response[i][j]):
                        tab_user[i][j]=' '
                        insert_null_tab_user(tab_user, tab_response, k, l)
                    else:
                        tab_user[i][j]=tab_response[i][j]
    return tab_user

def insert_input(tab_user, tab_response, i, j):
    # reveal the coordinates(i,j) in the array representing the user's inputs according to the response array
    x=tab_response[i][j]
    if x=='#':
        return False
    elif is_null(x):
        tab_user=insert_null_tab_user(tab_user, tab_response, i, j)
    else:
        tab_user[i][j]=tab_response[i][j]
    return tab_user

def empty_string(n):
    temp='  '
    for i in range(n):
        if len(temp)<=0:
            return temp
        temp=temp[1:]
    return temp
        
def display_games(tab_user,ligne, colonne):
    os.system('CLS')
    i=0
    j=0
    first_line=' '
    while (j<ligne):
        while i<colonne:
            if j==0:
                end_string=empty_string(len(str(i+1)))
                first_line+=('  '+str(i+1)+end_string)
            else:
                first_line+=('----')
            i+=1
        i=0
        while i<colonne:
            if i==0:
                screen=''
                if len(str(j+1))==1:
                    screen+=' '+str(j+1)
                else:
                    screen+=str(j+1)
            screen+=(' '+str(tab_user[j][i])+' |')
            i+=1
        i=0
        j+=1
        print(first_line)
        print(screen)
        first_line='-'
        screen='|'

def compareX(list1, list2, i, j):
    # returns true if a bomb is detected at coordinates (i,j)
    for m, val in enumerate(list1):
        if val==i:
            if list2[m]==j:
                return True
    return False

def check_tab_user(tab_user):
    # returns true if all squares have been revealed except bombs
    for i in range(len(tab_user[1])):
        for j in range(len(tab_user)):
            if tab_user[i][j]=='o':
                if compareX(list1,list2,i,j)==True:
                    pass
                else:
                    return False
    return True

os.system('CLS')
ligne=int(input('entrez un nombre de ligne:'))
colonne=int(input('entrez un nombre de colonne:'))
bomb_attack=int(input('entrez le nombre de bombes: '))
k=0
i=0
j=0

# user input array initialization
tab_user=[['o' for _ in range(ligne)]for _ in range(colonne)]  

# x coordinate of bombs
list1=[random.randint(0,ligne-1)]
# y coordinate of bombs
list2=[random.randint(0,colonne-1)]
# depositing bombs at coordinates x(list1) and y(list2)
while (k<bomb_attack-1):
    x=random.randint(0,ligne-1)
    y=random.randint(0,colonne-1)
    test=False
    for i, val in enumerate(list1):
        if val==x and list2[i]==y:
            test=False
            break
        else:
            test=True
    if test:
        list1.append(x)
        list2.append(y)
        k+=1

# response array initialization
response=[[0 for _ in range(ligne)]for _ in range(colonne)]   
# creation of the response array                  
for i in range(ligne):
    for j in range(colonne):
        response[i][j]=check_case(list1, list2, i , j)

# game launch
while(True): 
    display_games(tab_user,ligne, colonne) 
    coordX=int(input('Entrez x:'))-1                   
    coordY=int(input('Entrez y:'))-1
    if insert_input(tab_user, response, coordX, coordY)!=False:
        insert_input(tab_user, response, coordX, coordY)
    else:
        print('BOUM')
        break
    if check_tab_user(tab_user):
        display_games(tab_user,ligne, colonne)
        print('Bravo')
        break
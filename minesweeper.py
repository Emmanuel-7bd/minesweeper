import random
import os
os.system('CLS')

ligne=int(input('entrez un nombre de ligne:'))
colonne=int(input('entrez un nombre de colonne:'))
bomb_attack=int(input('entrez le nombre de bombes: '))
k=0
i=0
j=0
list1=[random.randint(0,ligne-1)]
list2=[random.randint(0,colonne-1)]

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
        
def is_bomb(list1, list2, a, b):
    for index , val in enumerate(list1):
        if val==a:
            if list2[index]==b:
                return True
    return False

def in_game(ligne, colonne, x,y):
    if x<0 or x>=ligne or y<0 or y>=colonne:
        return False
    return True

def check_case(list1, list2, a, b):
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

tab=[]  
response=[[0 for _ in range(ligne)]for _ in range(colonne)]                        
for i in range(ligne):
    for j in range(colonne):
        line=' '+str(check_case(list1, list2, i , j))+' '
        tab.append(line)
        response[i][j]=check_case(list1, list2, i , j)
    print(tab)
    tab=[]    

def is_null(a):
    return a==0

tab_user=[['x' for _ in range(ligne)]for _ in range(colonne)] 
def insert_null_tab_user(tab_user, tab_response, i , j):
    if in_game(ligne, colonne, i, j):
        if tab_user[i][j]=='x':
            x=i-1
            y=j-1
            for k in range(x,x+3):
                for l in range(y,y+3):
                    if is_null(tab_response[i][j]):
                        tab_user[i][j]=0
                        insert_null_tab_user(tab_user, tab_response, k, l)
                    else:
                        tab_user[i][j]=tab_response[i][j]
    return tab_user
                        


def insert_input(tab_user, tab_response, i, j):
    x=tab_response[i][j]
    if x=='#':
        return False
    elif is_null(x):
        tab_user=insert_null_tab_user(tab_user, tab_response, i, j)
    else:
        tab_user[i][j]=tab_response[i][j]
    
    return tab_user

def display_dubbel_tab(tab):
    disp=[]
    for i in range(len(tab[1])):
        for j in range(len(tab)):
            disp.append(tab[i][j])
        print(disp)
        disp=[]
        
def display_games(tab_user,ligne, colonne):
    os.system('CLS')
    i=0
    j=0
    first_line='-'
    screen='|'
    while (j<ligne):
        while i<colonne:
            first_line+=('----')
            i+=1
        i=0
        while i<colonne:
            screen+=(' '+str(tab_user[j][i])+' |')
            i+=1
        i=0
        j+=1
        print(first_line)
        print(screen)
        first_line='-'
        screen='|'

def compareX(list1, list2, i, j):
    for m, val in enumerate(list1):
        if val==i:
            if list2[m]==j:
                return True
    return False

def check_tab_user(tab_user):
    for i in range(len(tab_user[1])):
        for j in range(len(tab_user)):
            if tab_user[i][j]=='x':
                if compareX(list1,list2,i,j)==True:
                    pass
                else:
                    return False
    return True
    
        
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
        print('Bravo')
        break
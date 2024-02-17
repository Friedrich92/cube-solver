import sqlite3 
# X = X
# X' = X + 1
# X2 = X + 2
#________________________
# U = 1
# D = 4
# R = 7
# L = 10
# F = 13
# B = 16
combination = [0,0,0,0,0,0,0,0]
algorithem = []
# max = 18
con = sqlite3.connect('cube.db')
curs = con.cursor()
#curs.execute("""CREATE TABLE algorithims(alg STRING,orange_posision1 STRING,orange_posision2 STRING,orange_posision3 STRING,orange_posision4 STRING,orange STRING, orange STRING, blue STRING,red STRING)""")
    
def dbAlgorithemsInsert(alg,w1,w2,w3,w4,g,o,b,r):
    curs.execute(f"""INSERT INTO algorithems VALUES({alg},{w1},{w2},{w3},{w4},{g},{o},{b},{r},)""")
    

def translate():
    algorithem.clear()
    for item in combination:
        
        if item == 1:
            algorithem.append("U")
        
        if item == 2:
            algorithem.append("U'")
        
        if item == 3:
            algorithem.append("U2")

        if item == 4:
            algorithem.append("D")

        if item == 5:
            algorithem.append("D'")

        if item == 6:
            algorithem.append("D2")

        if item == 7:
            algorithem.append("R")

        if item == 8:
            algorithem.append("R'")

        if item == 9:
            algorithem.append("R2'")

        if item == 10:
            algorithem.append("L")

        if item == 11:
            algorithem.append("L'")

        if item == 12:
            algorithem.append("L2")

        if item == 13:
            algorithem.append("F")

        if item == 14:
            algorithem.append("F'")

        if item == 15:
            algorithem.append("F2")

        if item == 16:
            algorithem.append("B")

        if item == 17:
            algorithem.append("B'")
            
        if item == 18:
            algorithem.append("B2")


u_first = ['black','black','black','orange','black','black','black','black','black']
f_first = ['black','black','black','blue','black','black','black','red','black']
r_first = ['black','black','black','black','black','black','black','orange','black']
l_first = ['black','black','black','black','black','orange','black','black','black']
d_first = ['black','orange','black','black','black','orange','black','black','black']
b_first = ['black','black','black','black','black','black','black','black','black']

u_layer = []
f_layer = []
r_layer = []
l_layer = []
d_layer = []
b_layer = []

u_original = []
f_original = []
r_original = []
l_original = []
d_original = []
b_original = []

def first_reset():
    u_layer.clear()
    f_layer.clear()
    r_layer.clear()
    l_layer.clear()
    d_layer.clear()
    b_layer.clear()
    for item in u_first:
        u_layer.append(item)
    for item in r_first:
        r_layer.append(item)
    for item in l_first:
        l_layer.append(item)
    for item in f_first:
        f_layer.append(item)
    for item in b_first:
        b_layer.append(item)
    for item in d_first:
        d_layer.append(item)


def original_set():
    u_original.clear()
    f_original.clear()
    r_original.clear()
    l_original.clear()
    d_original.clear()
    b_original.clear()
    for item in u_layer:
        u_original.append(item)
    for item in f_layer:
        f_original.append(item)
    for item in r_layer:
        r_original.append(item)
    for item in l_layer:
        l_original.append(item)
    for item in d_layer:
        d_original.append(item)
    for item in b_layer:
        b_original.append(item)



def update():
    u_original.clear()
    f_original.clear()
    r_original.clear()
    l_original.clear()
    d_original.clear()
    b_original.clear()
    for i in u_layer:
        u_original.append(i)

    for i in f_layer:
        f_original.append(i)

    for i in r_layer:
        r_original.append(i)

    for i in l_layer:
        l_original.append(i)

    for i in d_layer:
        d_original.append(i)

    for i in b_layer:
        b_original.append(i)

def cube():
    print(u_layer)
    print(f_layer)
    print(r_layer)
    print(l_layer)
    print(d_layer)
    print(b_layer)


def replace_u(item,index):
    u_layer.pop(index)
    u_layer.insert(index,item)

def replace_d(item,index):
    d_layer.pop(index)
    d_layer.insert(index,item)

def replace_f(item,index):
    f_layer.pop(index)
    f_layer.insert(index,item)

def replace_b(item,index):
    b_layer.pop(index)
    b_layer.insert(index,item)

def replace_r(item,index):
    r_layer.pop(index)
    r_layer.insert(index,item)

def replace_l(item,index):
    l_layer.pop(index)
    l_layer.insert(index,item)


def cross_solved():
    if d_layer[1] == 'white' and f_layer[7] == 'green' and d_layer[3] == 'white' and d_layer[5] == 'white' and d_layer[7] == 'white' and r_layer[7] == 'red' and l_layer[7] == 'orange' and b_layer[7] == 'blue': 
        return True  
    
def turns():
    for item in combination:
        itemIndex = combination.index(item)
        if item == 1:
            replace_b(l_original[0],0)
            replace_b(l_original[1],1)
            replace_b(l_original[2],2)

            replace_f(r_original[0],0)
            replace_f(r_original[1],1)
            replace_f(r_original[2],2)

            replace_l(f_original[0],0)
            replace_l(f_original[1],1)
            replace_l(f_original[2],2)

            replace_r(b_original[0],0)
            replace_r(b_original[1],1)
            replace_r(b_original[2],2)

            replace_u(u_original[0],2)
            replace_u(u_original[1],5)
            replace_u(u_original[2],8)
            replace_u(u_original[3],1)
            replace_u(u_original[5],7)
            replace_u(u_original[6],0)
            replace_u(u_original[7],3)
            replace_u(u_original[8],6)
            update()




        if item == 2:
            replace_b(r_original[0],0)
            replace_b(r_original[1],1)
            replace_b(r_original[2],2)

            replace_f(l_original[0],0)
            replace_f(l_original[1],1)
            replace_f(l_original[2],2)

            replace_l(b_original[0],0)
            replace_l(b_original[1],1)
            replace_l(b_original[2],2)

            replace_r(f_original[0],0)
            replace_r(f_original[1],1)
            replace_r(f_original[2],2)

            replace_u(u_original[0],6)
            replace_u(u_original[1],3)
            replace_u(u_original[2],0)
            replace_u(u_original[3],7)
            replace_u(u_original[5],1)
            replace_u(u_original[6],8)
            replace_u(u_original[7],5)
            replace_u(u_original[8],2)
            update()
        
        if item == 3:
            replace_b(f_original[0],0)
            replace_b(f_original[1],1)
            replace_b(f_original[2],2)

            replace_f(b_original[0],0)
            replace_f(b_original[1],1)
            replace_f(b_original[2],2)

            replace_l(r_original[0],0)
            replace_l(r_original[1],1)
            replace_l(r_original[2],2)

            replace_r(l_original[0],0)
            replace_r(l_original[1],1)
            replace_r(l_original[2],2)

            replace_u(u_original[0],8)
            replace_u(u_original[1],7)
            replace_u(u_original[2],6)
            replace_u(u_original[3],5)
            replace_u(u_original[5],3)
            replace_u(u_original[6],2)
            replace_u(u_original[7],1)
            replace_u(u_original[8],0)
            update()
        
        if item == 4:
            replace_b(r_original[6],6)
            replace_b(r_original[7],7)
            replace_b(r_original[8],8)

            replace_f(l_original[6],6)
            replace_f(l_original[7],7)
            replace_f(l_original[8],8)

            replace_l(b_original[6],6)
            replace_l(b_original[7],7)
            replace_l(b_original[8],8)

            replace_r(f_original[6],6)
            replace_r(f_original[7],7)
            replace_r(f_original[8],8)

            replace_d(d_original[0],2)
            replace_d(d_original[1],5)
            replace_d(d_original[2],8)
            replace_d(d_original[3],1)
            replace_d(d_original[5],7)
            replace_d(d_original[6],0)
            replace_d(d_original[7],3)
            replace_d(d_original[8],6)
            update()



        if item == 5:
            replace_b(l_original[6],6)
            replace_b(l_original[7],7)
            replace_b(l_original[8],8)

            replace_f(r_original[6],6)
            replace_f(r_original[7],7)
            replace_f(r_original[8],8)

            replace_l(f_original[6],6)
            replace_l(f_original[7],7)
            replace_l(f_original[8],8)

            replace_r(b_original[6],6)
            replace_r(b_original[7],7)
            replace_r(b_original[8],8)

            replace_d(d_original[0],6)
            replace_d(d_original[1],3)
            replace_d(d_original[2],0)
            replace_d(d_original[3],7)
            replace_d(d_original[5],1)
            replace_d(d_original[6],8)
            replace_d(d_original[7],5)
            replace_d(d_original[8],2)
            update()
        

        
        if item == 6:
            replace_b(f_original[6],6)
            replace_b(f_original[7],7)
            replace_b(f_original[8],8)

            replace_f(b_original[6],6)
            replace_f(b_original[7],7)
            replace_f(b_original[8],8)

            replace_l(r_original[6],6)
            replace_l(r_original[7],7)
            replace_l(r_original[8],8)

            replace_r(l_original[6],6)
            replace_r(l_original[7],7)
            replace_r(l_original[8],8)

            replace_d(d_original[0],8)
            replace_d(d_original[1],7)
            replace_d(d_original[2],6)
            replace_d(d_original[3],5)
            replace_d(d_original[5],3)
            replace_d(d_original[6],2)
            replace_d(d_original[7],1)
            replace_d(d_original[8],0)
            update()
        
        if item == 7:
            replace_b(u_original[8],0)
            replace_b(u_original[5],3)
            replace_b(u_original[2],6)

            replace_f(d_original[2],2)
            replace_f(d_original[5],5)
            replace_f(d_original[8],8)

            replace_d(b_original[0],8)
            replace_d(b_original[3],5)
            replace_d(b_original[6],2)

            replace_u(f_original[2],2)
            replace_u(f_original[5],5)
            replace_u(f_original[8],8)

            replace_r(r_original[0],2)
            replace_r(r_original[1],5)
            replace_r(r_original[2],8)
            replace_r(r_original[3],1)
            replace_r(r_original[5],7)
            replace_r(r_original[6],0)
            replace_r(r_original[7],3)
            replace_r(r_original[8],6)
            update()
           
        if item == 8:
            replace_b(d_original[2],6)
            replace_b(d_original[5],3)
            replace_b(d_original[8],0)

            replace_f(u_original[2],2)
            replace_f(u_original[5],5)
            replace_f(u_original[8],8)

            replace_d(f_original[2],2)
            replace_d(f_original[5],5)
            replace_d(f_original[8],8)

            replace_u(b_original[0],8)
            replace_u(b_original[3],5)
            replace_u(b_original[6],2)

            replace_r(r_original[0],6)
            replace_r(r_original[1],3)
            replace_r(r_original[2],0)
            replace_r(r_original[3],7)
            replace_r(r_original[5],1)
            replace_r(r_original[6],8)
            replace_r(r_original[7],5)
            replace_r(r_original[8],2)
            update()

            

        if item == 9:
            replace_b(f_original[2],6)
            replace_b(f_original[5],3)
            replace_b(f_original[8],0)

            replace_f(b_original[0],8)
            replace_f(b_original[3],5)
            replace_f(b_original[6],2)

            replace_d(u_original[2],2)
            replace_d(u_original[5],5)
            replace_d(u_original[8],8)

            replace_u(d_original[2],2)
            replace_u(d_original[5],5)
            replace_u(d_original[8],8)

            replace_r(r_original[0],8)
            replace_r(r_original[1],7)
            replace_r(r_original[2],6)
            replace_r(r_original[3],5)
            replace_r(r_original[5],3)
            replace_r(r_original[6],2)
            replace_r(r_original[7],1)
            replace_r(r_original[8],0)
            update()

        if item == 10:
            replace_b(d_original[0],8)
            replace_b(d_original[3],5)
            replace_b(d_original[6],2)

            replace_f(u_original[0],0)
            replace_f(u_original[3],3)
            replace_f(u_original[6],6)

            replace_d(f_original[0],0)
            replace_d(f_original[3],3)
            replace_d(f_original[6],6)

            replace_u(b_original[2],6)
            replace_u(b_original[5],3)
            replace_u(b_original[8],0)

            replace_l(l_original[0],2)
            replace_l(l_original[1],5)
            replace_l(l_original[2],8)
            replace_l(l_original[3],1)
            replace_l(l_original[5],7)
            replace_l(l_original[6],0)
            replace_l(l_original[7],3)
            replace_l(l_original[8],6)
            update()

        if item == 11:
            replace_b(u_original[0],8)
            replace_b(u_original[3],5)
            replace_b(u_original[6],2)

            replace_f(d_original[0],0)
            replace_f(d_original[3],3)
            replace_f(d_original[6],6)

            replace_d(b_original[2],6)
            replace_d(b_original[5],3)
            replace_d(b_original[8],0)

            replace_u(f_original[0],0)
            replace_u(f_original[3],3)
            replace_u(f_original[6],6)

            replace_l(l_original[0],6)
            replace_l(l_original[1],3)
            replace_l(l_original[2],0)
            replace_l(l_original[3],7)
            replace_l(l_original[5],1)
            replace_l(l_original[6],8)
            replace_l(l_original[7],5)
            replace_l(l_original[8],2)
            update()

        
        if item == 12:
            replace_b(f_original[0],8)
            replace_b(f_original[3],5)
            replace_b(f_original[6],2)

            replace_f(b_original[2],6)
            replace_f(b_original[5],3)
            replace_f(b_original[8],0)

            replace_d(u_original[0],0)
            replace_d(u_original[3],3)
            replace_d(u_original[6],6)

            replace_u(d_original[0],0)
            replace_u(d_original[3],3)
            replace_u(d_original[6],6)

            replace_l(l_original[0],8)
            replace_l(l_original[1],7)
            replace_l(l_original[2],6)
            replace_l(l_original[3],5)
            replace_l(l_original[5],3)
            replace_l(l_original[6],2)
            replace_l(l_original[7],1)
            replace_l(l_original[8],0)
            update()

        if item == 13:
            replace_l(d_original[0],2)
            replace_l(d_original[1],5)
            replace_l(d_original[2],8)

            replace_r(u_original[6],0)
            replace_r(u_original[7],3)
            replace_r(u_original[8],6)

            replace_d(r_original[0],2)
            replace_d(r_original[3],1)
            replace_d(r_original[6],0)

            replace_u(l_original[2],8)
            replace_u(l_original[5],7)
            replace_u(l_original[8],6)

            replace_f(f_original[0],2)
            replace_f(f_original[1],5)
            replace_f(f_original[2],8)
            replace_f(f_original[3],1)
            replace_f(f_original[5],7)
            replace_f(f_original[6],0)
            replace_f(f_original[7],3)
            replace_f(f_original[8],6)
            update()

        if item == 14:
            replace_l(u_original[6],8)
            replace_l(u_original[7],5)
            replace_l(u_original[8],2)

            replace_r(d_original[2],0)
            replace_r(d_original[1],3)
            replace_r(d_original[0],6)

            replace_d(l_original[2],0)
            replace_d(l_original[5],1)
            replace_d(l_original[8],2)

            replace_u(r_original[0],6)
            replace_u(r_original[3],7)
            replace_u(r_original[6],8)

            replace_f(f_original[0],6)
            replace_f(f_original[1],3)
            replace_f(f_original[2],0)
            replace_f(f_original[3],7)
            replace_f(f_original[5],1)
            replace_f(f_original[6],8)
            replace_f(f_original[7],5)
            replace_f(f_original[8],2)
            update()

        if item == 15:
            replace_l(r_original[2],8)
            replace_l(r_original[5],5)
            replace_l(r_original[8],2)

            replace_r(l_original[0],6)
            replace_r(l_original[3],3)
            replace_r(l_original[6],0)

            replace_d(u_original[0],2)
            replace_d(u_original[1],1)
            replace_d(u_original[2],0)

            replace_u(d_original[6],8)
            replace_u(d_original[7],7)
            replace_u(d_original[8],6)

            replace_f(f_original[0],8)
            replace_f(f_original[1],7)
            replace_f(f_original[2],6)
            replace_f(f_original[3],5)
            replace_f(f_original[5],3)
            replace_f(f_original[6],2)
            replace_f(f_original[7],1)
            replace_f(f_original[8],0)
            update()

        if item == 16:
            replace_l(u_original[0],6)
            replace_l(u_original[1],3)
            replace_l(u_original[2],0)

            replace_r(d_original[6],8)
            replace_r(d_original[7],5)
            replace_r(d_original[8],2)


            replace_u(r_original[2],0)
            replace_u(r_original[5],1)
            replace_u(r_original[8],2)

            replace_d(l_original[0],6)
            replace_d(l_original[3],7)
            replace_d(l_original[6],8)

            replace_b(b_original[0],2)
            replace_b(b_original[1],5)
            replace_b(b_original[2],8)
            replace_b(b_original[3],1)
            replace_b(b_original[5],7)
            replace_b(b_original[6],0)
            replace_b(b_original[7],3)
            replace_b(b_original[8],6)
            update()

        if item == 17:
            replace_r(u_original[0],2)
            replace_r(u_original[1],5)
            replace_r(u_original[2],8)

            replace_l(d_original[6],0)
            replace_l(d_original[7],3)
            replace_l(d_original[8],6)

            replace_u(l_original[0],2)
            replace_u(l_original[3],1)
            replace_u(l_original[6],0)

            replace_d(r_original[2],8)
            replace_d(r_original[5],7)
            replace_d(r_original[8],6)

            replace_b(b_original[0],6)
            replace_b(b_original[1],3)
            replace_b(b_original[2],0)
            replace_b(b_original[3],7)
            replace_b(b_original[5],1)
            replace_b(b_original[6],8)
            replace_b(b_original[7],5)
            replace_b(b_original[8],2)
            update()

        if item == 18:
            replace_r(l_original[0],8)
            replace_r(l_original[3],5)
            replace_r(l_original[6],2)

            replace_l(r_original[2],6)
            replace_l(r_original[5],3)
            replace_l(r_original[8],0)

            replace_u(d_original[6],2)
            replace_u(d_original[7],1)
            replace_u(d_original[8],0)

            replace_d(u_original[0],8)
            replace_d(u_original[1],7)
            replace_d(u_original[2],6)

            replace_b(b_original[0],8)
            replace_b(b_original[1],7)
            replace_b(b_original[2],6)
            replace_b(b_original[3],5)
            replace_b(b_original[5],3)
            replace_b(b_original[6],2)
            replace_b(b_original[7],1)
            replace_b(b_original[8],0)
            update()

my_num = []
def refresh():
    first_reset()
    original_set()
    my_num.append(1)
    print(sum(my_num))
    
refresh()
turns()



def replace_combination(item,index):
    combination.pop(index)
    combination.insert(index,item)


def crack1():
    num = 0
    for i in range(19):
        refresh()
        replace_combination(num,0)
        num = num + 1
        turns()
        if cross_solved() == True:
            
            translate()
            print(algorithem)
            exit()

def crack2():
    num = 0
    for i in range(19):
        refresh()
        replace_combination(num,1)
        num = num + 1
        crack1()
        turns()
        if cross_solved() == True:
            
            translate()
            print(algorithem)
            exit()
  

def crack3():
    num = 0
    for i in range(19):
        refresh()
        replace_combination(num,2)
        num = num + 1
        crack1()
        crack2()
        turns()
        if cross_solved() == True:
            
            translate()
            print(algorithem)
            exit()
    

def crack4():
    num = 0
    for i in range(19):
        refresh()
        replace_combination(num,3)
        num = num + 1
        crack1()
        crack2()
        crack3()
        turns()
        if cross_solved() == True:
            
            translate()
            print(algorithem)
            exit()

def crack5():
    num = 0
    for i in range(19):
        refresh()
        replace_combination(num,4)
        num = num + 1
        crack1()
        crack2()
        crack3()
        crack4()
        turns()
        if cross_solved() == True:
            
            translate()
            print(algorithem)
            exit()

def crack6():
    num = 0
    for i in range(19):
        refresh()
        replace_combination(num,5)
        num = num + 1
        crack1()
        crack2()
        crack3()
        crack4()
        crack5()
        turns()
        if cross_solved() == True:
            
            translate()
            print(algorithem)
            exit()



def crack7():
    num = 0
    for i in range(19):
        refresh()
        replace_combination(num,6)
        num = num + 1
        crack1()
        crack2()
        crack3()
        crack4()
        crack5()
        crack6()
        turns()
        if cross_solved() == True:
            
            translate()
            print(algorithem)
            exit()

def crack8():
    num = 0 
    for i in range(19):
        refresh()
        replace_combination(num,7)
        num = num + 1
        crack1()

        crack2()
        crack3()
        crack4()
        crack5()
        crack6()
        crack7()
        turns()
        if cross_solved() == True:
            
            translate()
            print(algorithem)
            exit()
            

crack8()
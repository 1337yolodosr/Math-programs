import math #math.sqrt

import sys #sys.exit

import time #time.sleep




def Simultaneous_Equation_Solver():
    
    print('''In development
redirecting you to the quadratic solver
and thanks for trying Sho's solver system...''')
    time.sleep(3)
    Quadratic_Equation_Solver()

def Quadratic_Equation_Solver():
    data = input("Quadratic:")
    quad = ""
    for x in range(0, len(data)):
        if data[x] != " ":
            quad += data[x]
    quad += "+"
    sections = []
    base = 0
    for x in range(0, len(quad)):
        if quad[x] is "+" or quad[x] is "-":
            sections.append(quad[base:x])
            base = x
    print(sections)
    for x in range(0, len(sections)):
        if "x" in sections[x]:
            sav = sections[x][:sections[x].find("x")]
            if sav == "":
                sections[x] = 1
            else:
                sections[x] = int(sav)
        else:
            sections[x] = int(sections[x])
    a = sections[0]
    b = sections[1]
    c = sections[2]

    print(a,b,c)

    d = b**2-4*a*c # discriminant

    if d < 0:
        print ("This equation has no real solution")
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        print ("This equation has one solutions: "), x
    else:
        sol1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        sol2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        print ("This equation has following solutions: ", sol1, " or", sol2)

fn_map = {
    "quadratic": Quadratic_Equation_Solver,
    "simultaneous": Simultaneous_Equation_Solver
}

opt = input(" quadratic or simultaneous equation? (hit '9' to quit)")

if opt in fn_map:
    fn_map[opt]() # + argument list of course

elif '9' in opt:
    print("Thanks for trying!")
    time.sleep(1.5)
    sys.exit(0)

else:
    raise Exception("option %s not implemented" % (opt))
   
    

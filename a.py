want = []

def form_tri(w):
    return w * (w+1) // 2

def form_pent(w):
    return w * (3*w-1) // 2

def form_hex(w):
    return w * (2*w-1) 
no = int(input("Whats the number u don't want: "))
#code only works if 0, 1 or 40755 is input - not anymore hehe
found = False
while not found:
    for t in range (0,1000000):
        tri = form_tri(t)
        print("tri: ",tri)
        for p in range (0,1000000):
            pent = form_pent(p)
            print("pent: ",pent)
            if tri == pent:
                print ("tri = pent", pent)
                for n in range (0, 1000000):
                    hex = form_hex(n)
                    print("hex: ",hex)
                    if hex == pent and tri != no and tri != 0 and tri != 1:
                        want.append (tri)
                        found = True
                        break
                if found:
                    print("found value changed to true")
                    break
        
        if found:   
            print("we are in the outer loop")
            break
                

print ("The first value excluding the one u dont want that works is: ", want[-1])

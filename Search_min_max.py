x = [input(f"Numero {i+1}: \n") for i in range(0, 8)]

def search(operation):
    cont = 1
    valor = ""
    for k in x:
        for j in x:
            if x.index(k) == x.index(j):
                pass
            else:
                if valor != k:
                    cont = 0
                if eval(f" {k} {operation} {j}"):
                    valor = k
                    cont +=1
                    if cont == (len(x)-1):
                        return k
                else:
                    pass
                
print(f" Maior: {search('>')}")
print(f" Menor: {search('<')}")

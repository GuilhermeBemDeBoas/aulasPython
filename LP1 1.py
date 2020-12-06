def interativo(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return(a)
def recursivo(n):
    if n < 2:
        return(n)
    else:
        return(recursivo(n-1)+recursivo(n-2))
        
        

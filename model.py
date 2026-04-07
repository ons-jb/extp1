def produit (T):
    S=0
    for t in T:
        S*=t
        return S
data = [1,3,5]
prod=math.prod(data)
print("le produit est:", prod)

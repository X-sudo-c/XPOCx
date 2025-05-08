
#length = n
# s[k] is used for indexing -n <= k <0]
#what is the equivalent of j >= 0 such that j references the same element 




# index (positve):   0  1  2  3  4 
# character      :   h  e  l  l  o
# index (negative): -5 -4 -3 -2 -1 

s = "bombradino crocodilo"
n = len(s)


for k in range(-n,0):
    j = n + k
    print(j, k, f"{s[j]}  : {s[k]}") 
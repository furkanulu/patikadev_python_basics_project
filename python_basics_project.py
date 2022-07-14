# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları
# birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi,
# non-scalar verilerden de oluşabilir.
# Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# output: [1,'a','cat',2,3,'dog',4,5]

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
# Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

#--------------------------------------------------------------------

# input: [ [1,'a', ['cat'], 2], [[[3]] ,'dog' ] , 4, 5]

# output: [1,'a','cat',2,3,'dog',4,5]
def flatten_func(lst,flatten_list=[]):
    if lst == []:
        return lst
    else:
        for l in lst:
            if type(l)==list:
                flatten_func(l)
            else:
                flatten_list.append(l)
        return flatten_list

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]
def reverse_func(l):
    reverse_l=l[::-1]
    for i in range(len(reverse_l)):
        (reverse_l[i])=(reverse_l[i])[::-1]
    return reverse_l

def main():
    l1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    flatten_l=flatten_func(l1)
    l2=[[1, 2], [3, 4], [5, 6, 7]]
    reverse_l=reverse_func(l2)
    print("Düzleştirme fonksiyonu:\n")
    print(f"Input:{l1}\n")
    print(f"Output:{flatten_l}\n")
    print("------------------\n")
    print("Ters çevirme fonksiyonu:\n")
    print(f"Input:{l2}\n")
    print(f"Output:{reverse_l}")
    pass

if __name__=="__main__":
    main()
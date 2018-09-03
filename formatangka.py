print("========Soal Algoritma 3========")

bil = int(raw_input("Input Bilangan  : "))
pangkat = len(str(bil))-1
bil = int(str(bil)[::-1])

while(bil>0):
    print((bil%10)*(10**pangkat))
    pangkat -= 1
    bil = bil / 10

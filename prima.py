print("========Soal Algoritma 1========")

bil = int(raw_input("Masukan bilangan : "))
count = 0

for i in range(1,bil):
    if(bil % i == 0):
        count += 1

if count == 1 :
    print("Bilangan prima")
else :
    print("Bukan prima")

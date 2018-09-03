print("========Soal Algoritma 2========")

bil = int(raw_input("Input Bilangan fibbonaci : "))

Fibbo = [0,1,1]
if bil<=2  :
    print("Nilai bilangan: ",1)
else :
    for i in range(0,bil):
        if (i>=2):
            Fibbo.append(Fibbo[i-1] + Fibbo[i])
    print("Nilai bilangan : ",Fibbo[len(Fibbo)-1])

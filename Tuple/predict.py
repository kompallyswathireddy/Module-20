r= (1,0,0,1,0,0,0,1,1,0)
sunny=0
rainy=0


for i in range(len(r)):
    if r[i]==0:
        rainy+=1
    else:
        sunny +=1

if (sunny<rainy):
    print("Carry an umberella")
else:
    print("Good weather")
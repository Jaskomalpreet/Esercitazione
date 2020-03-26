from random import randint

def main(n):
    for i in range(n):
        print("*",end='')
    print("\n")

    
r = int(input())
if r>0:
  for p in range(r):
    main(p)
else:
    s = randint(1,100)
    p = randint(1,100)
    t=s-p
    main(t)

  


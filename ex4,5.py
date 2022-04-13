from socket import SOMAXCONN


n = int (input("n: "))

ac = 0
i = 1 
txt = ""

while i <=n:
    ac = ac + i
    txt = txt + str(i) + " + "
    i = i+1

txt = txt + str(i) + " ="     
ac = ac + 1
print (txt, ac)

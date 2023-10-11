def sipelgas():
    a = input()
    b = input()
    c = input()
    kuubik = a.split(" ")
    sipelgas = b.split(" ")
    mesi = c.split(" ")
    if b[0]==c[0]:
        q = ((int(b[1])-int(c[1]))**2) + (int(b[2])-int(c[2])**2)**0.5
    if b[1]==c[1]:
        q = ((int(b[0])-int(c[0]))**2) + (int(b[2])-int(c[2])**2)**0.5
    if b[2]==c[2]:
        q = ((int(b[1])-int(c[1]))**2) + (int(b[0])-int(c[0])**2)**0.5

    print(q)

sipelgas()
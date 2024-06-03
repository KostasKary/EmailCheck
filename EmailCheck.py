def EmailCheck():
    e=input("Your email")
    fp=0
    fg=0
    ft=0
    fpg=0
    pg=0
    pa=0
    pt=0
    for i in range(0,len(e)):
        if e[i]=="@":
            fp=1
            pa=i
    for i in range(0,len(e)):
        if e[i]==".":
            ft=1
            pa=i
    for i in range(0,len(e)):
        if e[i].isalpha() and fg==0:
            t=i
            fg=1
            pg=i
    if pg<pa:
        fpg=1
    if fp==1 and ft==1 and fpg==1:
        print("Valid email")
    elif fp==0:
        print("You need an @")
    elif ft==0:
        print("You need a .")
    elif fpg==0:
        print("Put a letter before the @")

EmailCheck()
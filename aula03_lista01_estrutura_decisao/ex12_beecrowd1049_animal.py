"""In this problem, your job is to read three Portuguese words.
These words define an animal according to the table below, from left to right.
After, print the chosen animal defined by these three words."""

a = input("vertebrado ou invertebrado? ")

if (a=='vertebrado'):
    b = input("ave ou mamifero? ")
    if (b=='ave'):
        c = input("carnivoro ou onivoro? ")
        if (c=='carnivoro'):
            print("aguia")
        else:
            print("pomba")
    else:
        c = input("onivoro ou herbivoro?")
        if (c=='onivoro'):
            print("homem")
        else:
            print("vaca")
else:
    b = input("inseto ou anelideo?")
    if (b=='inseto'):
        c = input("hematofago ou herbivoro? ")
        if (c=='hematofago'):
            print("pulga")
        else:
            print("lagarta")
    else:
        c = input("hematofago ou onivoro?")
        if (c=='hematofago'):
            print("sanguessuga")
        else:
            print("minhoca")
    
    
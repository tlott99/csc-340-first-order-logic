import pytholog as pl

def kings():
    kb = pl.KnowledgeBase("Kings")

    #TELL
    kb(
        [
          "king(john)",   # John is a King
          "person(richard)",  #Richard is a person
          "person(X)  :- king(X)  ", #If X is a king then X is also a person
          "brother(john,richard)",
          "brother(richard,john)",

        ]
    )  

    #ASK
    print(kb.query(pl.Expr("king(john)")))
    print(kb.query(pl.Expr("king(richard)")))
    print(kb.query(pl.Expr("brother(richard,X)")))
    pass

def animals():
    kb = pl.KnowledgeBase("Animals")
    kb(
        [
        "animals(X) :- mammals(X)",
        "mammals(X) :- feline(X))",
        "feline(X) :- cat(X)",
        "feline(X) :- lion(X)",
        "mammals(X) :- canine(X)",
        "canine(X) :- dog(X)",
        "canine(X) :- wolf(X)",
        "animals(X) :- reptile(X)",
        "reptile(X) :- turtle(X)",
        "dog(sparky)",
        "cat(marlow)",
        "wolf(bigboi)",
        "lion(alex)",
        "turtle(raphael)",
        ]
    )
    print(kb.query(pl.Expr("animals(raphael)")))
    print(kb.query(pl.Expr("canine(sparky)")))
    print(kb.query(pl.Expr("animals(X)")))
    print(kb.query(pl.Expr("mammals(X)")))
    pass

def kinship():
    kb = pl.KnowledgeBase("kinship")
    kb(
        [    # and = "," or = ";"
        "mother(M,C) :- female(M) , parent(M,C)",  
        "parent(P,C) :- child(C,P)", 
        "grandparent(G,C) :- parent(G,P) , parent(P,C)",
        "female(melanie)",
        "child(eden,melanie)",
        "child(eden,kenny)",
        "child(kenny,joan)"
        ]
    )
    print(kb.query(pl.Expr("grandparent(joan,eden)")))
    pass

def main():
    # print("hello.")
    # kinship()
    # kings()
    animals()

if __name__ == "__main__":
    main()
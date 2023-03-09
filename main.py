import pytholog as pl

def kings():
    kb = pl.KnowledgeBase("Kings")
    kb(
        [
        "king(john)",
        "person(richard)"
        "person(X) :- king(X)",
        "brother(john,richard)",
        "brother(richard,john)"
        ]
    )
    print(kb.query(pl.Expr("king(john)")))
    print(kb.query(pl.Expr("king(richard)")))
    print(kb.query(pl.Expr("brother(richard,X)")))
    pass

def animals():
    kb = pl.KnowledgeBase("Animals")
    kb(
        [
        "animals(mammals)",
        "mammals(feline)",
        "feline(cat)",
        "feline(lion)",
        "mammals(canine)",
        "canine(dog)",
        "canine(wolf)",
        "animals(reptile)",
        "reptile(turtle)"

        ]
    )
    pass

def kinship():
    kb = pl.KnowledgeBase("Kinship")
    kb(
        [
        "mother(M,C) :- female(M) , parent(M,C)",
        "parent(P,C) :- child(C,P)",
        "grandparent(G,C) :- parent(G,P) , parent(P,C)",

        "female(melanie)",
        "child(eden,melanie)",
        "child(eden,kenny)",
        "child(kenny,joan)",
        ]
    )
    print(kb.query(pl.Expr("grandparent(joan,eden)")))
    pass

def main():
    # print("hello.")
    kinship()
    # kings()
    animals()

if __name__ == "__main__":
    main()
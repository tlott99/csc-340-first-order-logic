import pytholog as pl

def kings():
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
    pass

def main():
    print("hello.")
    kinship()
    kings()
    animals()

if __name__ == "__main__":
    main()
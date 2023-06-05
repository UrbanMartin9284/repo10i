alap = int(input("Kérem az alapot: "))
kitevo = int(input("Kérem a kitevőt: "))


def hatvanyozas():
    if kitevo == 0:
        print(1)
    elif kitevo == 1:
        print(alap)
    else:
        print(alap ** kitevo)

hatvanyozas()


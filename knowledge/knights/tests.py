from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A can only be knight or knave but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # if A is a knight, then he doesnt lie
    Implication(AKnight, And(AKnight, AKnave)),
    # If he is a knave, he lies
    Implication(AKnave, Not(And(AKnight, AKnave)))
)


def main():

    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]

    for symbol in symbols:
        if model_check(knowledge0, symbol):
            print(f"    {symbol}")


if __name__ == "__main__":
    main()

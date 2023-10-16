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
    # A is either a knight or a knave, not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # Sentence is true if A is a knight
    Implication(AKnight, And(AKnight, AKnave)),

    # Sentence is false is A is a knave
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either a knight or a knave, not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B is either a knight or a knave, not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    # A's sentence is true if A is a knight
    Implication(AKnight, And(AKnave, BKnave)),
    # A's sentence is false if A is a knave
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is either a knight or a knave, not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B is either a knight or a knave, not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    # A's sentence is true if A is a knight
    Implication(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    # A's sentence is false if A is a knave
    Implication(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),

    # B's sentence is true if B is a knight
    Implication(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))),
    # B's sentence is false if B is a knave
    Implication(BKnave, Not(Or(And(AKnave, BKnight), And(AKnight, BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A is either a knight or a knave, not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B is either a knight or a knave, not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # C is either a knight or a knave, not both
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),


    # B's first sentence is true if B is a knight
    Implication(BKnight,
                # ---> A's sentence is true if A is a knight
                Implication(AKnight, AKnave)),
    # B's first sentence is true if B is a knight
    Implication(BKnight,
                # ---> A's sentence is false if A is a knave
                Implication(AKnave, AKnight)),

    # B's first sentence is false if B is a knave
    Implication(BKnave,
                # ---> A's sentence is true if A is a knight
                Implication(AKnight, AKnight)),
    # B's first sentence is false if B is a knave
    Implication(BKnave,
                # ---> A's sentence is false if A is a knave
                Implication(AKnave, AKnave)),

    # B's second sentence is true if B is a knight
    Implication(BKnight, CKnave),
    # B's second sentence is false if B is a knave
    Implication(BKnave, CKnight),

    # C's sentence is true if C is a knight
    Implication(CKnight, AKnight),
    # C's sentence is false if C is a knave
    Implication(CKnave, AKnave),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

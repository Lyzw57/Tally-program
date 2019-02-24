def get_score(tally: str):
    scores = {}

    for char in tally:
        player = char.lower()
        if player not in scores.keys():
            scores[player] = 0
        if char.islower():
            scores[player] += 1
        else:
            scores[player] -= 1

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    for example in ('abcde', 'dbbaCEDbdAacCEAadcB', 'EbAAdbBEaBaaBBdAccbeebaec'):
        print(get_score(example))
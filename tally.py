def get_score(tally: str):
    scores = {}

    for char in tally:
        player = char.lower()
        score = scores.get(player, 0)
        change = 1 if char.islower() else - 1
        scores[player] = score + change

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    for example in ('abcde', 'dbbaCEDbdAacCEAadcB', 'EbAAdbBEaBaaBBdAccbeebaec'):
        print(get_score(example))
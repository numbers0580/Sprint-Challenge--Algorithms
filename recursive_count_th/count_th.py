'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Assume the word = thattherethickthingamajigthough
    tally = 0

    if len(word) < 2:
        # Not long enough to contain the letters we're searching for. Move along, move along.
        return 0
    else:
        if word[:2] == "th":
            print(f"Examining {word[0:2]}, tally was {tally}")
            tally += 1
            print(f"Tally is now {tally}")
        else:
            print(f"Nothing here. Tally was {tally}")
            tally = tally
            print(f"Tally is still {tally}")

        # Move start of word by 1, add in tally. This should create tally += tally += tally += tally += tally + 1 = 5
        tally += count_th(word[1:])
        # Found error. I had the above line tabbed over one too many times.

        return tally

# Created this so I could test my own recursion, since I was unsure of how to keep track of the tally
if __name__ == "__main__":
    gibberish = "thattherethickthingamajigthough"

    print(f"thattherethickthingamajigthough has {count_th(gibberish)} th's")
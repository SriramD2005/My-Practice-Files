from collections import defaultdict
memoization = defaultdict(int)
def findOrbs(notes, portion):
    global memoization
    orbs = []
    for comb in notes[portion]:
        currOrbs = 0
        for ing in comb:
            if ing in memoization.keys():
                currOrbs += memoization[ing]
            else:
                if ing in notes.keys():
                    #print(ing,":::")
                    currOrbs += findOrbs(notes, ing)
                    #print(currOrbs)
                else:
                    #currOrbs += 1
                    memoization[ing] = 0
        orbs.append((currOrbs, len(comb)))
    minOrbs = min(orbs)
    minOrbs = minOrbs[0] + minOrbs[1] - 1
    memoization[portion] = minOrbs
    return minOrbs

if __name__ == "__main__":
    N = int(input())
    notes = defaultdict(list)
    for i in range(N):
        inp = input()
        inp = inp.split("=")
        #print(inp)
        inp[1] = inp[1].split("+")
        if inp[0] in notes:
            notes[inp[0]].append(inp[1])
        else:
            notes[inp[0]] = [inp[1]]
    target = input()
    #print(notes)
    print(findOrbs(notes, target), end = "")
    #print(memoization)
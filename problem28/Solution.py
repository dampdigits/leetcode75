def predictPartyVictory(senate):
    radiant, dire, i = [], [], 0
    
    for ch in senate:
        if ch == 'R': radiant.append(i)
        else: dire.append(i)
        i += 1

    while radiant and dire:
        if radiant.pop(0) < dire.pop(0): radiant.append(i)
        else: dire.append(i)
        i += 1

    return 'Radiant' if radiant else 'Dire'

def main():
    senate = 'RRD'
    print(predictPartyVictory(senate))

if __name__ == "__main__":
    main()

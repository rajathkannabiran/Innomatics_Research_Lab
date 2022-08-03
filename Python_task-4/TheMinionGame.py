def minion_game(string):
    # your code goes here
    s = len(string)
    final_score,f = 0,0
    for i in range(s):
        if string[i] in 'AEIOU':
            final_score += (s-i)
        else:
            f += (s-i)
    if final_score > f:
        print(f"Kevin {final_score}")
    elif final_score < f:
        print(f"Stuart {f}")
    elif f == final_score:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
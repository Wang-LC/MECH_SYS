def letter_count(text, letter):
    ans = text.lower().count(letter.lower())
    return ans

if __name__ == '__main__':
    if letter_count('halLway', 'l') == 2 and letter_count('halLway', 'L') == 2:
        print("words passed!")

def commonCharacterCount(s1, s2):
    character_count = 0
    unique_one = set(s1)
    unique_two = set(s2)
    combination = [letter for letter in unique_one if letter in unique_two]
    for letter in combination:
        count_s1 = s1.count(letter)
        count_s2 = s2.count(letter)
        if  count_s1 <= count_s2:
            character_count += count_s1
        else:
            character_count += count_s2
    return character_count
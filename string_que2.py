sentence = "pw skill data science pro "
vowel_count = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowel_count += 1

print("Number of vowels in the sentence:", vowel_count)

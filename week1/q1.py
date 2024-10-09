def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for character in word:
        if character in vowels:
            count+=1
    return count
    
print(count_vowels("hello"))
print(count_vowels("DataScience"))
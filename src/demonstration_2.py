"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
# def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str

    Output:
    bool
    """
    # Your code here

def are_words_sorted(words, alpha_order):
    order_dict = {}
​
    for index, char in enumerate(alpha_order):
        order_dict[char] = index
    # loop over our words
    for i in range(len(words) - 1):
        word_1 = words[i]
        word_2 = words[i + 1]
        # Compare the current word to next
        # go letter by letter
        for j in range(min(len(word_1), len(word_2))):
            letter_1 = word_1[j]    
            letter_2 = word_2[j]
            if letter_1 == letter_2:
                continue
            index_1 = order_dict[letter_1]
            index_2 = order_dict[letter_2]
            if index_1 > index_2:
                return False
            else:
                break
        else:
            # if loop ends naturally, check the words length
            return False
    
    return True
​
words = ["lambda","school"] 
order = "hlabcdefgijkmnopqrstuvwxyz"
​
print(are_words_sorted(words, order))
​
words = ["lambda","lamb"] 
order = "abcdefghijklmnopqrstuvwxyz"
​
print(are_words_sorted(words, order))
​
words = ["were","where","yellow"]
order = "habcdefgijklmnopqrstuvwxyz"
​
print(are_words_sorted(words, order))
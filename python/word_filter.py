"""
Word Filter and Counter Function

Objective:
Write a function named 'word_filter_counter' that filters and counts specific words in a given text.

Function Parameters:
1. text (string): The text from which words will be filtered and counted.
2. filter_words (list of strings): A list of words to be filtered out from the text.

Instructions:
- The function should filter out the words from the text that are present in the filter_words list. The comparison should be case-insensitive.
- The function should return a dictionary. In this dictionary, the keys are the filtered words, and the values are the counts of how often these words appeared in the text.
- The text may contain punctuation marks and spaces. Only whole words, separated by spaces or punctuation, should be considered.

Example Test Cases:
1. word_filter_counter("Hello world, hello!", ["hello"]) should return a dictionary with the count of occurrences of "hello".
2. word_filter_counter("The quick brown fox.", ["the"]) should return a dictionary with the count of occurrences of "the".
3. word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]) should return a dictionary with the counts of occurrences of "is", "this", and "just".
4. word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]) should return a dictionary with the counts of occurrences of "we", "the", and "or".
"""

import string
def word_filter_counter(text, filter_words):
    # Your code goes here
    # Implement the logic to filter words and count their occurrences

 # Convert filter words to lowercase and convert to lowercase 转换为小写
    filter_words = [word.lower() for word in filter_words]

# Remove punctuation from text    移除标点符号
    #string.punctuation包含了所有标准的ASCII标点符号
    #str.maketrans 用于创建字符映射转换表
    #translate 方法用于执行实际的字符替换或删除操作
    text = text.translate(str.maketrans('', '', string.punctuation))
 # Split the text into words  分割文本为单词 
    words = text.split()
# Count occurrences of each word in filter_words 计算单词出现次数
    count_dict = {}
    for word in filter_words:
        count_dict[word] = words.count(word)

    return count_dict

    

   
# Test cases
print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  # Expected output: {'hello': 2}
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}


    


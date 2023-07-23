def sorting_the_sentence_1859(s):
    word_list = s.strip().split(" ")
    sorted_words = [""] * len(word_list)
    for word in word_list:
        index = int(word[-1])
        sorted_words[index - 1] = word[:-1]
    return " ".join(sorted_words)


def make_the_string_great_1544(s):
    stack = []
    for char in s:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


def jewels_and_stones_771(jewels, stones):
    total_count = 0
    for element in jewels:
        total_count = total_count + stones.count(element)
    return total_count


def longest_common_prefix_14(strs):
    if not str:
        return ""
    common_prefix = ""
    zip_list = list(zip(*strs))
    for index, element in enumerate(zip_list):
        if len(set(zip_list[index])) == 1:
            common_prefix += element[0]
        else:
            break
    return common_prefix


def merge_string_alternately_1768(word1, word2):
    min_length = min(len(word1), len(word2))
    sub_result_string = [word1[i] + word2[i] for i in range(min_length)]
    return "".join(sub_result_string) + word1[min_length:] + word2[min_length:]


def sort_the_people_2418(names, heights):
    return [name for _, name in sorted(zip(heights, names), reverse=True)]


def uncommon_word_form_two_sentences(s1, s2):
    from collections import Counter
    total_words = s1.split(" ") + s2.split(" ")
    return [key for key, value in Counter(total_words).items() if value == 1]


def count_the_number_of_consistent_strings(allowed, words):
    allowed = set(allowed)
    return len([element for element in words if set(element).issubset(allowed)])


def shuffle_string_1528(s, indices):
    new_list = [None] * len(s)
    for index, element in enumerate(indices):
        new_list[element] = s[index]
    return "".join(new_list)


def percentage_of_letter_in_string_2278(s, letter):
    return round((s.count(letter) / len(s)) * 100)



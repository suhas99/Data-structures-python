class MySolution:
    # O(w * n *logn)( w is number of words) and n is the longest word | Ow(n) space
    def find_anagrams(self, words_list):
        anagram = {}
        for word in words_list:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram:
                anagram[sorted_word].append(word)
            else:
                anagram[sorted_word] = [word]
        return list(anagram.values())


if __name__ == "__main__":
    solution_test_one = MySolution()
    print(solution_test_one.find_anagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))

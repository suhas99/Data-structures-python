class MySolution:
    # Time o(n) | Space O(1)

    def check_palindrome_solution1(self, string):
        low = 0
        high = len(string) - 1
        while low < high:
            if string[low] != string[high]:
                return False
            low += 1
            high -= 1
        return True

    # space 0(n) | Time

    def check_palindrome_solution2(self, string):
        string_as_list = list(string)
        return string_as_list == string_as_list[::-1]


solution_first = MySolution()
print(solution_first.check_palindrome_solution1("abba"))

solution_second=MySolution()
print(solution_second.check_palindrome_solution2("ghjkmn"))


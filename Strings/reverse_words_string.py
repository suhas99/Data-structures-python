# without built in
class MySolution:

    def reverse_solution(self, string):
        temp = ''
        new_array = []
        for char in string:
            if char == ' ':
                new_array.append(temp)
                temp = ''
            else:
                temp += char
        if temp:
            new_array.append(temp)
        return " ".join(new_array[::-1])


if __name__=="__main__":
    solution_one=MySolution()
    print(solution_one.reverse_solution("i am sde2 for 3 years"))

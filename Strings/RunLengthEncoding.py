class MySolution:

    def run_length_encoding_solution_one(self,string):
        run_len = 1
        encoded_array = []
        for i in range(1, len(string)):
            current_element = string[i]
            previous_element = string[i - 1]
            if current_element != previous_element or run_len == 9:
                encoded_array.append(str(run_len))
                encoded_array.append(previous_element)
                run_len = 0
            run_len += 1

        encoded_array.append(str(run_len))
        encoded_array.append(string[len(string) - 1])
        return "".join(encoded_array)


if __name__ == '__main__':
    solution_first=MySolution()
    print(solution_first.run_length_encoding_solution_one("aabbcddd"))

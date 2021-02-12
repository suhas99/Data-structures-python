class MySolution:
    # O(n) time O(n) space
    def caesar_cipher_encryptor_solution_one(self, string, key):
        low = 0
        high = len(string) - 1
        new_string = ''
        while low <= high:
            if ord(string[low]) + key > 122:
                new_string += chr(96 + (ord(string[low]) + key) - 122)
            else:
                new_string += chr(ord(string[low]) + key)
            low += 1
        return new_string

    def caesar_cipher_encryptor_solution_two(self, string, key):
        new_key = key % 26
        new_letter = []
        for letter in string:
            new_letter.append(self.get_new_letter(letter, new_key))
        return "".join(new_letter)

    def get_new_letter(self, letter, key):
        new_letter_number = ord(letter) + key
        if new_letter_number <= 122:
            return chr(new_letter_number)
        else:
            return chr(96 + new_letter_number % 122)


if __name__ == '__main__':
    solution_first = MySolution()
    print(solution_first.caesar_cipher_encryptor_solution_one("xyz", 2))

    solution_second=MySolution()
    print(solution_second.caesar_cipher_encryptor_solution_two("xyz",2))

class StringClass:

    @staticmethod
    def all_unique_characters(string):
        """
        Determines if given string has all unique characters

        Time complexity: O(n)
        Space complexity : O(1)

        :param string: given string
        :return: boolean
        """
        if len(string) > 128:  # assuming ASCII characters only
            return False
        charset = set()
        for s in string:
            if s in charset:
                return False
            else:
                charset.add(s)
        return True

    @staticmethod
    def are_permutations(str1, str2):
        """
        Checks if given two strings are permutations of each other

        Uses python sorted method to sort the string, then compares them

        Time Complexity: O(m log m) + O(n log n)
        Space Complexity: O(2)
        :param str1:
        :param str2:
        :return: boolean
        """
        if len(str1) != len(str2):
            return False

        return sorted(str1) == sorted(str2)

    @staticmethod
    def are_permutations2(str1, str2):
        """
        Checks if given two strings are permutations of each other

        Creates dicts with character counts and compares if both are similar

        Time Complexity: O(m+n)
        Space Complexity: O(2)
        :param str1:
        :param str2:
        :return: boolean
        """
        if len(str1) != len(str2):
            return False
        dict1 = {}
        dict2 = {}
        for s in str1:
            if s in dict1:
                dict1[s] += 1
            else:
                dict1[s] = 1
        for s in str2:
            if s in dict2:
                dict2[s] += 1
            else:
                dict2[s] = 1
        if dict1 == dict2:
            return True
        else:
            return False

    @staticmethod
    def replace_white_space(string, n):
        """
        Replace whitespaces in string with %20 (in-place)

        Time Complexity: O(n)
        Space Complexity: O(1)

        :param string:
        :param n: length of final string
        :return:
        """
        count = len(string)
        string_array = list(string)
        for i in range(n - 1, 0, -1):
            char = string_array[i]
            if char != " ":
                count -= 1
                string_array[count] = char
            else:
                string_array[count-1] = "0"
                string_array[count-2] = "2"
                string_array[count-3] = "%"
                count -= 3
        return "".join(string_array)

    @staticmethod
    def check_if_permutation_palindrome(string):
        """
        Checks if a given method could have a permutation that is a palindrome

        Time Complexity: O(n)
        Space Complexity: O(1)

        :param string:
        :return: boolean
        """
        count_dict = {}
        for char in list(string):
            if char in count_dict:
                count_dict[char] += 1  ## TODO: Instead of storing as number, we can store as a boolean value, where True represents even & False represents odd.
                                        # TODO: Final value of count isn't actually used, we only check to see if it's odd/even
            else:
                count_dict[char] = 1
        odd_count = 0
        for k, v in count_dict.items():
            if v % 2 != 0:
                odd_count += 1
            if odd_count > 1:
                return False
        return True

    @staticmethod
    def is_one_edit_away(str1, str2):
        """
        Given two strings check if one is 1-edit away from the other

        Time Complexity: -
        Space Complexity: -

        :param str1:
        :param str2:
        :return: boolean
        """
        if len(str1) == len(str2):
            return StringClass.check_for_one_edit_replacement(str1, str2)
        elif len(str1) - len(str2) == 1:
            return StringClass.check_for_one_edit_insertion(str1, str2)
        elif len(str2) - len(str1) == 1:
            return StringClass.check_for_one_edit_insertion(str2, str1)
        else:
            return False

    @staticmethod
    def check_for_one_edit_replacement(s1, s2):
        """
        Checks if s1 is one character's replacement away from s2

        Time Complexity: O(n), n is the length of both s1 & s2
        Space Complexity:

        :param s1:
        :param s2:
        :return: boolean
        """
        replacement_count = 0
        for i, j in zip(s1, s2):
            if i != j:
                replacement_count += 1
                if replacement_count > 1:
                    return False
        return True

    @staticmethod
    def check_for_one_edit_insertion(s1, s2):
        """
        Checks if s1 is one character's insertion away from s2

        Time Complexity: O(n), n is the length of the shorter string

        :param s1:
        :param s2:
        :return: boolean
        """
        j = 0
        for i in range(len(s2)):
            if s1[i] != s2[j]:
                if i != j:
                    return False
                else:
                    continue
            j += 1
        return True


if __name__ == "__main__":
    s1 = "Hello"
    print("Are string characters unique in {}? {}".format(s1, StringClass.all_unique_characters(s1)))

    s2 = "Bye"
    print("Are string characters unique in {}? {}".format(s2, StringClass.all_unique_characters(s2)))

    s3 = "hello"
    s4 = "ohel"
    print("Is \"{}\" a permutation of \"{}\"? {}".format(s3, s4, StringClass.are_permutations(s3, s4)))
    print("Is \"{}\" a permutation of \"{}\"? {}".format(s3, s4, StringClass.are_permutations2(s3, s4)))

    s5 = "hello world  "
    print("Convert spaces in \"{}\" to %20: {}".format(s5, StringClass.replace_white_space(s5, 11)))

    s6 = "kettleelttek"
    print("Does \"{}\" have a permutation with a palindrome? {}".format(s6, StringClass.check_if_permutation_palindrome(s6)))

    s7 = "kaya"
    s8 = "maya"
    print("Is \"{}\" one edit away from \"{}\"?: {}".format(s7, s8, StringClass.is_one_edit_away(s7, s8)))

    s9 = "kayak"
    print("Is \"{}\" one edit away from \"{}\"?: {}".format(s7, s9, StringClass.is_one_edit_away(s7, s9)))

    s10 = "beer"
    print("Is \"{}\" one edit away from \"{}\"?: {}".format(s7, s10, StringClass.is_one_edit_away(s7, s10)))

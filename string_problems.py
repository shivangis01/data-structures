from typing import List
from pandas import *


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

    @staticmethod
    def compress_string(string):
        """

        :param string:
        :return:
        """
        str_list = []
        current = string[0]
        count = 0

        str_list.append(current)
        for c in string:
            if c == current:
                count += 1
            else:
                str_list.append(str(count))
                current = c
                count = 1
                str_list.append(current)
        str_list.append(str(count))

        if len(str_list) > len(string):
            return string
        else:
            return "".join(str_list)


    @staticmethod
    def _is_substring(s1, s2):
        """
        Checks if s1 is a substring of s2
        :param s1:
        :param s2:
        :return: boolean
        """
        return s1 in s2

    @staticmethod
    def is_rotation(s1, s2):
        """
        Check if s1 can be rotated in a way to give s2

        Time Complexity: O(n) - n is length of each string

        :param s1:
        :param s2:
        :return: boolean
        """
        if len(s1) != len(s2):
            return False
        first_char = s2[0]
        n = len(s1)
        for i in range(n):
            if s1[i] == first_char:
                if StringClass._is_substring(s1[i:n-1], s2) and StringClass._is_substring(s1[0:i-1], s2):
                    return True
        return False

    @staticmethod
    def create_zero_matrix(matrix: List[List[int]]):
        """
        Given a MxN matrix, for any cell that contains '0', set all its rows & cols to zero

        Time Complexity: O(2MN) ~ O(MN)
        Space Complexity: O(M+N) ~ O(N)

        :param matrix:
        :return:
        """
        zero_rows = []
        zero_cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
        return matrix

    @staticmethod
    def rotate_matrix(matrix: List[List[int]]):
        """
        Rotate an N x N matrix clockwise, in-place

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        :param matrix:
        :return:
        """
        n = len(matrix)
        for i in range(int(n/2)):
            first = i
            last = n - i - 1
            for j in range(i, last):
                offset = j - i

                # top-left
                temp = matrix[first][j]

                # bottom-left -> top-left
                matrix[first][j] = matrix[last - offset][first]

                # bottom-right -> bottom-left
                matrix[last - offset][first] = matrix[last][last - offset]

                # top-right -> bottom-right
                matrix[last][last - offset] = matrix[j][last]

                # top-left -> top-right
                matrix[j][last] = temp

        return matrix


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

    s11 = "aaaabbcccddddaa"
    print("Compressed version of \"{}\": {} ".format(s11, StringClass.compress_string(s11)))

    s12 = "abcdef"
    print("Compressed version of \"{}\": {} ".format(s12, StringClass.compress_string(s12)))

    s13 = "tomcat"
    s14 = "cattom"
    s15 = "attcom"
    print("Is \"{}\" a rotation of \"{}\"?: {}".format(s14, s13, StringClass.is_rotation(s14, s13)))
    print("Is \"{}\" a rotation of \"{}\"?: {}".format(s15, s13, StringClass.is_rotation(s15, s13)))

    m1 = [[1,2,0], [4,5,6], [0,8,9]]
    new_matrix = StringClass.create_zero_matrix(m1)
    print("New matrix looks like:")
    print(DataFrame(new_matrix))

    m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Rotate Matrix:")
    print(DataFrame(m2))
    new_matrix = StringClass.rotate_matrix(m2)
    print("New matrix looks like:")
    print(DataFrame(new_matrix))

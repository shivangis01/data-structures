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
        :param string:
        :param n: length of final string
        :return:
        """
        count = n
        string_array = list(string)
        for i in range(len(string_array) - 1, 0, -1):
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


if __name__ == "__main__":
    s1 = "Hello"
    print("Are string characters unique in {}? {}".format(s1, StringClass.all_unique_characters(s1)))

    s2 = "Bye"
    print("Are string characters unique in {}? {}".format(s2, StringClass.all_unique_characters(s2)))

    s3 = "hello"
    s4 = "ohel"
    print("Permutations? {}".format(StringClass.are_permutations(s3, s4)))
    print("Permutations? {}".format(StringClass.are_permutations2(s3, s4)))

    s5 = "hello world"
    print("Remove spaces: {}".format(StringClass.replace_white_space(s5, 11)))

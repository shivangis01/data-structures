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


if __name__ == "__main__":
    str1 = "Hello"
    print("Are string characters unique in {}? {}".format(str1, StringClass.all_unique_characters(str1)))

    str2 = "Bye"
    print("Are string characters unique in {}? {}".format(str2, StringClass.all_unique_characters(str2)))
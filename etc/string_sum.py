import os


def string_sum(string1, string2):
    string1_length = len(string1)
    string2_length = len(string2)
    result = ""

    string2_index = string2_length - 1
    string1_index = string1_length - 1
    c = 0
    while string1_index != -1 or string2_index != -1:
        if string1_index == -1:
            num1 = 0
        else:
            num1 = int(string1[string1_index])
            string1_index -= 1
        if string2_index == -1:
            num2 = 0
        else:
            num2 = int(string2[string2_index])
            string2_index -= 1
        x = (num2 + num1) + c
        c = 0
        if x > 9:
            x -= 10
            c += 1
        result += str(x)
    return result[::-1]


if __name__ == '__main__':
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    string1 = input()
    string2 = input()

    result = string_sum(string1, string2)
    fptr.write(result + "\n")
    fptr.close()

"""
1239847109283740192783409187234
98112341234987273649812753498127634
"""
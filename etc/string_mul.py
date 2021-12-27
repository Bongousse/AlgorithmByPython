import os


def string_mul(string1, string2):
    string1_length = len(string1)
    string2_length = len(string2)
    result = []
    place = 0
    for string2_index in range(string2_length - 1, -1, -1):
        q = ""
        c = 0
        num2 = int(string2[string2_index])
        for string1_index in range(string1_length - 1, -1, -1):
            num1 = int(string1[string1_index])
            x = (num2 * num1) + c
            if string1_index == 0:
                q = str(x) + q
            else:
                q = str(x % 10) + q
                if x > 9:
                    c = x // 10
                else:
                    c = 0
        result.append(int(''.join(q)) * (10 ** place))
        place += 1
    return sum(result)


if __name__ == '__main__':
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    string1 = input()
    string2 = input()

    result = string_mul(string1, string2)
    fptr.write(result)
    fptr.close()


"""
1239847109283740192783409187234
1239847109283740192783409187234
"""
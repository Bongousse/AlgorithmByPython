import os


def string_reverse(string1):
    string_split = string1.split(" ")
    result = ""
    for item in string_split:
        result += item[::-1] + " "
    return result


if __name__ == '__main__':
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    string1 = input()

    result = string_reverse(string1)
    fptr.write(result + "\n")
    fptr.close()

"""
ab cde
 ab cde  
  ab  cde  
"""
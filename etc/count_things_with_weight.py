import os


def solution(weight):
    weight.sort(reverse=True)

    answer = 0
    while len(weight) != 0:
        current_weight_sum = weight.pop()
        remove_weight = []
        for current_weight in weight:
            if current_weight_sum + current_weight <= 3:
                current_weight_sum += current_weight
                remove_weight.append(current_weight)
        for r_weight in remove_weight:
            weight.remove(r_weight)
        answer += 1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    # fptr = open("output.txt", "w")
    weight_count = int(input().strip())
    weight = []
    for _ in range(weight_count):
        weight_item = float(input().strip())
        weight.append(weight_item)

    result = solution(weight)
    fptr.write(str(result) + "\n")
    fptr.close()

"""
5
1.4
1.01
2.4
1.01
1.01

4
1.4
1.991
1.01
1.32
"""
def solution(sentence, keyword, skips):
    index = 0
    k_index = 0
    s_index = 0
    answer = ""
    while s_index < len(skips):
        skip = skips[s_index]
        k = keyword[k_index % len(keyword)]
        if k in sentence[index:]:
            next_k_index = sentence[index:].index(k)
            if index + next_k_index < index + skip:
                answer += sentence[index:index + next_k_index + 1] + k
                index += next_k_index + 1
            else:
                if index + skip > len(sentence) + 1:
                    break
                answer += sentence[index:index + skip] + k
                index += skip
        else:
            if index + skip > len(sentence) + 1:
                break
            answer += sentence[index:index + skip] + k
            index += skip
        s_index += 1
        k_index += 1
    answer += sentence[index:]
    return answer


sentence = "i love coding"
keyword = "mask"
skips = [0, 0, 3, 2, 3, 4]
print(solution(sentence, keyword, skips))

sentence = "i love coding"
keyword = "mode"
skips = [0, 10]
print(solution(sentence, keyword, skips))

sentence = "abcdefghi"
keyword = "axyz"
skips = [3, 9, 0, 1]
print(solution(sentence, keyword, skips))

sentence = "encrypt this sentence"
keyword = "something"
skips = [0, 1, 3, 2, 9, 2, 0, 3, 0, 2, 4, 1, 3]
print(solution(sentence, keyword, skips))
"""seoncrmypett thihisng ssenteonmcee"""
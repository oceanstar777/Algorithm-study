def solution(participant, completion):
    ans_dct = {}
    hash_sum = 0
    for runner in participant:
        key = hash(runner)
        ans_dct[key] = runner
        hash_sum += key
    for runner in completion:
        key = hash(runner)
        hash_sum -= key

    answer = ans_dct[hash_sum]
    return answer

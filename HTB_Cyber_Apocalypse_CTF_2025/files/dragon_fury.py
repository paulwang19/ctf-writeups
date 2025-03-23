
def find_damage_combination(subarrays, target):
    max_value = 0
    for subarray in subarrays:
        max_value += max(subarray)
    
    # array dp: index represents the target
    #           array value represents the combination of the target value
    dp = [[]] * (max_value + 1)
    
    for target_value in subarrays[0]:
        dp[target_value] = [target_value]
    
    for subarray_index in range(1, len(subarrays)):
        new_dp = [[]] * (max_value + 1)
        for prev_target in range(len(dp)):
            if dp[prev_target]:
                for current_round_value in subarrays[subarray_index]:
                    new_dp[prev_target + current_round_value] = list.copy(dp[prev_target])  # deep copy
                    new_dp[prev_target + current_round_value].append(current_round_value)
        
        dp = new_dp
    
    return dp[target]

def main():
    round_damages_list = eval(input())
    target = int(input())
    result_list = find_damage_combination(round_damages_list, target)
    print(result_list)

main()
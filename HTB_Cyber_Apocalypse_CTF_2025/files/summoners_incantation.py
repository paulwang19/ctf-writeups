
def max_sum_nonadjacent(token_list):
    dp = [0] * len(token_list)
    dp[0] = token_list[0]
    dp[1] = token_list[1] if token_list[1] > token_list[0] else token_list[0]
    
    for i in range(2, len(token_list)):
        select_current_value = dp[i - 2] + token_list[i]
        dp[i] = select_current_value if select_current_value > dp[i - 1] else dp[i - 1]
    
    return dp[-1]

def main():
    input_text = input()
    token_list = eval(input_text)
    max_sum = max_sum_nonadjacent(token_list)
    print(max_sum)

main()
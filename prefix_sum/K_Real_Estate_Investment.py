num_test_case = int(input())
for test_case in range(num_test_case):
    r, c, l = list(map(int, input().split(" ")))
    matrix = [[0 for _ in range(c+1)] for __ in range(r+1)]
    psa = [[0 for _ in range(c+1)] for __ in range(r+1)]
    # Tính b và mảng cộng dồn
    for i in range(1, r+1):
        row = list(map(int, input().split(" ")))
        for j in range(1, c+1):
            matrix[i][j] = row[j-1] - l
            psa[i][j] = psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + matrix[i][j]
    best_profit = 0
    best_cost = 0
    for r1 in range(1, r+1):
        for r2 in range(r1, r+1):
            col_profit_arr = [0 for _ in range(c+1)]
            #Tính sum của profit theo cột
            for cj in range(1, c+1):
                col_profit_arr[cj] = psa[r2][cj] - psa[r1-1][cj] - psa[r2][cj-1] + psa[r1-1][cj-1]
            # Tính max_sum_sequence
            min_ps_col_profit = float("INF")
            max_col_profit = -float("INF")
            ps_col_profit = [0 for _ in range(c+1)]
            begin_col, min_length = 0, 0
            for i in range(1, c+1):
                ps_col_profit[i] = col_profit_arr[i] + ps_col_profit[i-1]
                # Tìm min_prefix_sum và index của cột của giá trị này
                if min_ps_col_profit >= ps_col_profit[i-1]:
                    begin_col = i
                    min_ps_col_profit = ps_col_profit[i-1]
 
                # Tìm giá trị max và index của cột có giá trị này
                if max_col_profit < max(max_col_profit, ps_col_profit[i] - min_ps_col_profit):
                    max_col_profit = max(max_col_profit, ps_col_profit[i] - min_ps_col_profit)
                    min_length = i - begin_col + 1
            # Tính diện tích
            cost = min_length*(r2 - r1 + 1)*l
            if best_profit < max_col_profit:
                best_profit = max_col_profit
                best_cost = cost
            elif best_profit == max_col_profit:
                best_cost = min(best_cost, cost)
 
    print(f"#{test_case+1}", best_profit, best_cost)
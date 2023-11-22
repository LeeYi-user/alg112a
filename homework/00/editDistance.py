def editDistance(a, b, i, j, dp = {}):
    if i == len(a) and j == len(b): # 如果已經比完 a 字串和 b 字串
        return 0 # 就回傳 0
    elif i == len(a): # 如果只有比完 a 字串
        return len(b) - j # 就回傳剩下還沒比的 b 字串長度
    elif j == len(b): # 如果只有比完 b 字串
        return len(a) - i # 就回傳剩下還沒比的 a 字串長度

    if (i, j) not in dp: # 如果從當前索引對開始的字串沒有比較過
        if a[i] == b[j]: # 如果在當前索引對下的字符相同
            ans = editDistance(a, b, i + 1, j + 1, dp) # 就什麼都不用做 (直接繼續比較)
        else: # 否則就嘗試三種編輯路線
            insert = 1 + editDistance(a, b, i, j + 1, dp) # 把 b 字串的字符插入 a 字串 (然後繼續比較)
            delete = 1 + editDistance(a, b, i + 1, j, dp) # 刪除 a 字串的字符 (然後繼續比較)
            replace = 1 + editDistance(a, b, i + 1, j + 1, dp) # 取代 a 字串的字符 (然後繼續比較)
            ans = min(insert, delete, replace) # 選擇能達成最小編輯距離的路線

        dp[(i, j)] = ans # 紀錄結果

    return dp[(i, j)] # 回傳從當前索引對開始的字串比較結果

a = "ATGCAATCCC"
b = "ATGATCCG"

print(editDistance(a, b, 0, 0))

# 台科大資管 Python 實作作業作答區

---

## 基本資料

學號： B11xxxxxx
系級： 資管系大一
姓名： 王小明

## 一、 原始碼分析報告 (Static Analysis) (20%)

### 變數與邏輯對照表

| 原始變數名稱 | 代表意義 (Business Logic) | 建議修正名稱 |
|---|---|---|
| Q1 a (in p_proc) | 分解後的輸入字串 | split_text |
| Q2 b (in p_proc) | 轉換輸入字串，變成 dict | text_dict |
| Q3 cate_dict | 各類型分類的 dict | category_dict |

### 壞味道 (Code Smells) 診斷

請列出原程式碼中至少 5 個嚴重的設計問題，並說明為什麼不好

Q1： 缺乏異常處理機制（Error Handling） int(a[1]) 與 p1[1].split("@@") 等處完全沒檢查格式。若使用者輸入非數字或不符格式的字串，程式會直接報錯並崩潰（Crash），穩定性極差。

Q2： 自創非標準資料格式（Fragile File Format） 使用 -- 與 @@ 作為分隔符號極其脆弱。若使用者的項目名稱內含這些符號，讀取邏輯就會毀損。應改用 JSON 或 CSV 等標準格式。

Q3： 全局變數濫用（Global State Dependency）：data_list 被多個函數直接修改。這會導致測試困難，且隨著專案擴大，追蹤是誰修改了資料會變成一場災難，應改以參數傳遞與回傳值處理。

Q4： 神祕命名與硬編碼索引（Magic Numbers & Naming）： 變數如 a, b, p1 完全無法表達商業邏輯，且 a[0], a[1] 等硬編碼索引讓程式碼難以閱讀，後續維護者難以理解資料結構。

Q5： 低效的檔案 I/O 操作： save() 每次存檔都重新複寫整個檔案，且未確保檔案指標正確關閉（雖然有 .close()，但用 with open 更安全）。在資料量大時性能不佳且容易因斷電導致資料遺失。

> 可參考以下 Code Smells！

1. Line 3~4 全局變數（壞習慣 1：隨意使用全局變數）
2. Line 7,11 # 壞習慣 2：神祕的變數命名，完全看不懂 a, b, c 是什麼
3. Line 11 # 壞習慣 3：硬編碼的索引，且混雜了字串與型別轉換 # 這裡的邏輯是：項目/金額/類別
4. Line 16,18 # 壞習慣 4：極其低效的檔案寫法，每次存檔都重新開啟並用奇怪的格式
5. Line 25,26 # 壞習慣 5：手動解析混亂的格式，容易出錯
6. Line 36 # 壞習慣 6：完全沒有防錯機制，輸入空白或格式不對會直接 Crash
7. Line 39 # 壞習慣 7：在結束時才做複雜運算，且邏輯重複 # 統計分類邏輯寫得非常混亂
8. Line 51 # 壞習慣 8：字串切割邏輯脆弱
9. Line 60 # 壞習慣 9：排版混亂，沒有格式化輸出
10. Line 64 # 壞習慣 10：隱藏功能（未說明的後門）

---

## 二、 Vibe-Coding 協作紀錄 (30%)

請記錄你如何引導 GitHub Copilot 進行重構。

### 1. 關鍵 Prompt 紀錄

請貼出你對 AI 下達過最有效的 3 個 Prompt：

```log
Prompt A： 請將這段 Python 程式碼重構。將資料儲存格式從 txt 改為 json，並引入 try-except 機制處理使用者輸入。

Prompt B： 請實施模組化設計，將原本的全局變數 data_list 改為以類別 (Class) 封裝的 DataManager，並將檔案路徑設為初始化參數。

Prompt C： 請美化 show 指令的輸出結果，改用 tabulate 函式庫或 f-string 對齊，讓支出表格看起來一目了然。
```

### 2. AI 錯誤處理

AI 在撰寫過程中是否有出錯？（例如：漏寫了某個功能、語法錯誤）你是如何發現並請它修正的？

- 發現的問題： AI 在初次重構時，漏掉了原本 exit 時需要顯示的「分類總額統計」功能。
- 修正的對話： 我告訴它：「在 exit 邏輯中，請加上一段迴圈，使用 dictionary 或 collections.Counter 重新統計各類別的金額總計後再退出。」

---

## 三、 成果驗證與測試 (30%)

確保你的 `refined_tracker.py` 功能正確。

### 1. 測試結果截圖 (Terminal)

>> ![alt text](image.png)

請貼上執行程式並輸入 show 後，顯示資料清單的截圖（或文字紀錄）。

### 2. 產出的資料檔案格式

請貼上重構後生成的 records.json 前幾行內容：

```json
[
    {"n": "breakfast", "p": 100, "t": "eat"}, 
    {"n": "bus", "p": 20, "t": "walk"}, 
    {"n": "dinner", "p": 150, "t": "eat"}
]
```

## 四、 Git 提交紀錄 (Commit History) (20%)

請執行 git log --oneline 並將最近的筆紀錄貼在此處，以證明你的開發流程。

```log
10a7ca3 (HEAD -> master) doc: Example answer
ebfcbd2 (origin/master, origin/HEAD) Init Commit
```

請附上你的 GitHub Repository 連結：

```log
https://github.com/fan9704/NTUST-Final
```

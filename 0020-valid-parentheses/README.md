# 20. Valid Parentheses

เช็กว่า `()[]{}` จับคู่และเรียงลำดับถูกไหม นับเปิดกับปิดให้เท่ากันยังไม่พอ เพราะ `)(` ก็เท่ากันแต่ผิด วิธีหลักคือ stack: เจอเปิด push เจอปิดเช็กว่าบนสุดเป็นคู่ของมันแล้ว pop จบแล้ว stack ต้องว่าง

- เวลา O(n) พื้นที่ O(n)
- เคสที่ควรเตรียม: สตริงว่าง, ปิดก่อนเปิด, คู่คนละชนิด (`(]`), เปิดค้าง (`((`)

| | |
|---|---|
| โค้ด | [valid_parentheses.py](valid_parentheses.py) |
| เทส | [test_valid_parentheses.py](test_valid_parentheses.py) |
| บทความเต็ม | https://blog.showkhun.co/blog/leetcode-valid-parentheses/ |
| โจทย์ต้นฉบับ | https://leetcode.com/problems/valid-parentheses/ |

รันเทสในโฟลเดอร์นี้:

```bash
python3 -m unittest -v
```

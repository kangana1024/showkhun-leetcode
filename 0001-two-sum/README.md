# 1. Two Sum

หาสองตำแหน่งในอาเรย์ที่บวกกันได้เท่า `target` วิธีหลักคือ hash map รอบเดียว: เดินทีละตัว คิด `need = target - value` ถ้า `need` เคยผ่านมาแล้วก็ตอบ ถ้ายังไม่เคย จดค่าตัวนี้ลงแมป

- ลองทุกคู่ O(n²) → hash map เวลา O(n) แลกพื้นที่ O(n)
- กับดัก: คืน index ไม่ใช่ค่า และห้ามจับคู่ตัวเอง

| | |
|---|---|
| โค้ด | [two_sum.py](two_sum.py) |
| เทส | [test_two_sum.py](test_two_sum.py) |
| บทความเต็ม | https://blog.showkhun.co/blog/leetcode-two-sum/ |
| โจทย์ต้นฉบับ | https://leetcode.com/problems/two-sum/ |

รันเทสในโฟลเดอร์นี้:

```bash
python3 -m unittest -v
```

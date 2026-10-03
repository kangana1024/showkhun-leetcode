# 3. Longest Substring Without Repeating Characters

หาความยาว substring ที่ยาวที่สุดที่ไม่มีตัวซ้ำ วิธีหลักคือ sliding window: ถือหน้าต่าง left–right และจำตำแหน่งล่าสุดของแต่ละตัว ถ้าตัวที่เจอซ้ำอยู่ในหน้าต่าง ให้กระโดด left ไปหลังตำแหน่งเดิมทันที

- `abcabcbb` → `abc` = 3 · เวลา O(n) แต่ละตัวผ่านรอบเดียว
- จุดพลาด `dvdf`: ตัวซ้ำต้องอยู่ในหน้าต่าง (`last[ch] >= left`) ก่อนถึงจะกระโดด
- มี brute force ไว้เทียบคำตอบในเทส

| | |
|---|---|
| โค้ด | [longest_substring.py](longest_substring.py) |
| เทส | [test_longest_substring.py](test_longest_substring.py) |
| บทความเต็ม | https://blog.showkhun.co/blog/leetcode-3-longest-substring-without-repeating/ |
| คลิปสั้น | https://youtube.com/shorts/5n6Cs3O3iT0 |
| โจทย์ต้นฉบับ | https://leetcode.com/problems/longest-substring-without-repeating-characters/ |

รันเทสในโฟลเดอร์นี้:

```bash
python3 -m unittest -v
```

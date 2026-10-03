# Showkhun LeetCode

โค้ด Python ประกอบคลิปสั้น LeetCode ของ [Showkhun Lab](https://www.youtube.com/@Showkhun-Lab) และบทความใน [Showkhun Blog](https://blog.showkhun.co/tags/leetcode/) เริ่มจากโจทย์ที่เจอบ่อยในสัมภาษณ์งาน แต่ละโฟลเดอร์มีโค้ด เทส และลิงก์บทความ

| # | โจทย์ | วิธีหลัก | เวลา | โค้ด |
|---|---|---|---|---|
| 1 | Two Sum | hash map รอบเดียว | O(n) | [0001-two-sum](0001-two-sum) |
| 3 | Longest Substring Without Repeating Characters | sliding window + ตำแหน่งล่าสุด | O(n) | [0003-longest-substring-without-repeating-characters](0003-longest-substring-without-repeating-characters) |
| 20 | Valid Parentheses | stack | O(n) | [0020-valid-parentheses](0020-valid-parentheses) |
| 121 | Best Time to Buy and Sell Stock | จำราคาต่ำสุด | O(n) | [0121-best-time-to-buy-and-sell-stock](0121-best-time-to-buy-and-sell-stock) |
| 200 | Number of Islands | flood fill (DFS / BFS) | O(แถว × คอลัมน์) | [0200-number-of-islands](0200-number-of-islands) |

## รันเทส

ใช้ Python 3.9 ขึ้นไป ไม่ต้องติดตั้งอะไรเพิ่ม

```bash
for d in 0*/; do (cd "$d" && python3 -m unittest -v); done
```

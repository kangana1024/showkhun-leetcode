# 200. Number of Islands

`1` คือบก `0` คือน้ำ บกที่ติดกันสี่ทิศนับเป็นเกาะเดียว วิธีหลักคือ flood fill: สแกนตาราง เจอบกใหม่นับ +1 แล้วจมทั้งเกาะไม่ให้นับซ้ำ

- ตารางตัวอย่างในเทสมี 3 เกาะ · แนวทแยงไม่นับว่าติดกัน
- เวลา O(แถว × คอลัมน์) · มีทั้ง DFS และ BFS — เกาะใหญ่ใน Python ใช้ BFS เลี่ยง recursion limit

| | |
|---|---|
| โค้ด | [number_of_islands.py](number_of_islands.py) |
| เทส | [test_number_of_islands.py](test_number_of_islands.py) |
| บทความเต็ม | https://blog.showkhun.co/blog/leetcode-200-number-of-islands/ |
| คลิปสั้น | https://youtube.com/shorts/8tcDQItqIKg |
| โจทย์ต้นฉบับ | https://leetcode.com/problems/number-of-islands/ |

รันเทสในโฟลเดอร์นี้:

```bash
python3 -m unittest -v
```

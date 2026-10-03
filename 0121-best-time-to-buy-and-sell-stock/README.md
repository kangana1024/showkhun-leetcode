# 121. Best Time to Buy and Sell Stock

ซื้อหนึ่งครั้ง ขายทีหลังหนึ่งครั้ง ให้กำไรมากที่สุด วิธีหลักคือจำราคาต่ำสุดที่เคยเห็น แล้วถามทุกวันว่าถ้าขายวันนี้ได้กำไรเท่าไหร่

- `[7, 1, 5, 3, 6, 4]` → ซื้อ 1 ขาย 6 กำไร 5 · ราคาลดตลอดตอบ 0
- เวลา O(n) พื้นที่ O(1) · มี brute force ไว้เทียบคำตอบในเทส
- เป็นโจทย์อัลกอริทึมที่มองย้อนหลัง ไม่ใช่คำแนะนำการลงทุน

| | |
|---|---|
| โค้ด | [best_time_to_buy_and_sell_stock.py](best_time_to_buy_and_sell_stock.py) |
| เทส | [test_best_time_to_buy_and_sell_stock.py](test_best_time_to_buy_and_sell_stock.py) |
| บทความเต็ม | https://blog.showkhun.co/blog/leetcode-121-best-time-buy-sell-stock/ |
| โจทย์ต้นฉบับ | https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ |

รันเทสในโฟลเดอร์นี้:

```bash
python3 -m unittest -v
```

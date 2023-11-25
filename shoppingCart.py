class ProductList:
    def __init__(self, prdtname, prdtprice, prdtgst, prdtqty):
        self.prdtname = prdtname
        self.prdtprice = prdtprice
        self.prdtgst = prdtgst
        self.prdtqty = prdtqty

cart = [
    ProductList("Leather", 1100, 18, 1),
    ProductList("Umbrella", 900, 12, 4),
    ProductList("Cigarette", 200, 28, 3),
    ProductList("Honey", 100, 0, 2)
]

max_gst_prdt = None;
max_gst_amt = 0;
for pro in cart:
    gst_amt = pro.prdtprice * pro.prdtgst / 100 * pro.prdtqty
    if gst_amt >= max_gst_amt:
        max_gst_amt = gst_amt
        max_gst_prdt = pro

totalamt = 0
for pro in cart:
    if pro.prdtprice >= 500:
        dis = pro.prdtprice * 5 / 100
        pro.prdtprice -= dis

    totalamt += pro.prdtprice * pro.prdtqty

print("Product with which we paid Maximum GST Amount : ", max_gst_prdt.prdtname)
# print("Max GST : ", max_gst_amt)
print("Total Amount to be PAID to the Shop Keeper: Rs.", totalamt)

# total amount to be paid : 5022 ?
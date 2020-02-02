# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com

from drawBot import *
import math

# [W]IDTH, [H]EIGHT, [M]ARGIN, [F]FONT-SIZE
# Note: 1 inch = 72 units
W,H,M,F = 612,792,54,72

# GRID
def grid():
    stroke(0)
    strokeWidth(1)
    lineCap("round")
    stpX, stpY = 0, 0
    incX, incY = 72, 72
    for x in range(8):
        polygon(((M)+stpX, M),
                ((M)+stpX, (H-(F*2))-(M+((F/4)*2))))
        stpX += incX
    for y in range(8):
        polygon((M, (M)+stpY),
                (W-(M), (M)+stpY))
        stpY += incY

# NEW PAGE
def new_page():
    newPage(W, H)

# MAIN
new_page()
grid() # Toggle for grid view
stroke(None)

fontSize(F*2.35)
font("fonts/Inter-ExtraBold.otf")
text("2", M+(F*5.6), M+(F*7.24))

fontSize(F)
text("February", M-4, M+(F*8))
tracking(-6)
text("2020", M-4, M+(F*7))

fontSize(F/4)
tracking(None)
text("Mon", (M+2)+(F*0), (M+(F*7))-20)
text("Tue", (M+2)+(F*1), (M+(F*7))-20)
text("Wed", (M+2)+(F*2), (M+(F*7))-20)
text("Thr", (M+2)+(F*3), (M+(F*7))-20)
text("Fri", (M+2)+(F*4), (M+(F*7))-20)
text("Sat", (M+2)+(F*5), (M+(F*7))-20)
text("Sun", (M+2)+(F*6), (M+(F*7))-20)

text("1",   (M+2)+(F*5), (M+(F*6))-20)
text("2",   (M+2)+(F*6), (M+(F*6))-20)

text("3",   (M+2)+(F*0), (M+(F*5))-20)
text("4",   (M+2)+(F*1), (M+(F*5))-20)
text("5",   (M+2)+(F*2), (M+(F*5))-20)
text("6",   (M+2)+(F*3), (M+(F*5))-20)
text("7",   (M+2)+(F*4), (M+(F*5))-20)
text("8",   (M+2)+(F*5), (M+(F*5))-20)
text("9",   (M+2)+(F*6), (M+(F*5))-20)

text("10",  (M+2)+(F*0), (M+(F*4))-20)
text("11",  (M+2)+(F*1), (M+(F*4))-20)
text("12",  (M+2)+(F*2), (M+(F*4))-20)
text("13",  (M+2)+(F*3), (M+(F*4))-20)
text("14",  (M+2)+(F*4), (M+(F*4))-20)
text("15",  (M+2)+(F*5), (M+(F*4))-20)
text("16",  (M+2)+(F*6), (M+(F*4))-20)

text("17",  (M+2)+(F*0), (M+(F*3))-20)
text("18",  (M+2)+(F*1), (M+(F*3))-20)
text("19",  (M+2)+(F*2), (M+(F*3))-20)
text("20",  (M+2)+(F*3), (M+(F*3))-20)
text("21",  (M+2)+(F*4), (M+(F*3))-20)
text("22",  (M+2)+(F*5), (M+(F*3))-20)
text("23",  (M+2)+(F*6), (M+(F*3))-20)

text("24",  (M+2)+(F*0), (M+(F*2))-20)
text("25",  (M+2)+(F*1), (M+(F*2))-20)
text("26",  (M+2)+(F*2), (M+(F*2))-20)
text("27",  (M+2)+(F*3), (M+(F*2))-20)
text("28",  (M+2)+(F*4), (M+(F*2))-20)
text("29",  (M+2)+(F*5), (M+(F*2))-20)

saveImage("pdfs/2020-02.pdf")
saveImage("images/2020-02.png")

# Name: Sophie Avery
# Time spent: ~1 hour

from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    return [data.count(i) for i in range(max(data) + 1)]
#1b
def print_histogram(hist:list[int]) -> None:
    [print(*[str(i) + ":"] + ["*" for j in range(hist[i])]) for i in range(len(hist))]


#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:
    # should deal with larger numbers -- fix that lmao
    rect_width = width / len(hist)
    rect_height = (height / max(hist)) - 10
    gw = GWindow(width, height)
    brick_color = "#4E0E04"
    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        rect.set_line_width(5)
        gw.add(rect)
    x = 0
    for i in range(len(hist)):
        y = height - rect_height
        for j in range(hist[i]):
            my_rect(x,y,rect_width,rect_height,brick_color)
            y -= rect_height
        x += rect_width


# Some testing printouts for your use!
PI_DIGITS = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 5, 8, 9, 7, 9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test


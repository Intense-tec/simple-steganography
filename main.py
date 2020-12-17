"""
Name : main.py.py
Author : OBR01
Contect : brich.oussama@gmail.com
Time    : 17/12/2020 16:16
Desc:
"""
import png


def encode(input_path, output_path):
    rgb_rows = []

    r = png.Reader(input_path)
    print(r.read()[2])

    for row in r.asRGB()[2]:
        rgb_rows.append(list(row))
    get_rgb_ordered(rgb_rows)


# Order RGB list (as : [(R,G,B), (R,G,B), ...]
def get_rgb_ordered(rgb_rows):
    rgb_pixels_list = []
    for row in rgb_rows:
        rgb_pixels = [row[x:x + 3] for x in range(0, len(row), 3)]
        rgb_pixels_list.append(rgb_pixels)
    print(rgb_pixels_list)
    return rgb_pixels_list


#################
# Main Function #
#################
if __name__ == "__main__":
    print("Staring...")
    image_input_path = "./images/basketBall.png"
    image_output_path = ""

    encode(image_input_path, image_output_path)


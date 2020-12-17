"""
Name : main.py.py
Author : OBR01
Contact : brich.oussama@gmail.com
Time    : 17/12/2020 16:16
Desc:
"""
import png


# Encode text in input image and save it with the change
def encode(input_path, text, output_path):
    rgb_rows = []

    r = png.Reader(input_path)
    print(r.read()[2])

    for row in r.asRGB()[2]:
        rgb_rows.append(list(row))
    get_rgb_ordered(rgb_rows)

    ascii = convert_text_to_ascii("Hello Alice !")
    print(ascii)


# Convert text to ascii list
def convert_text_to_ascii(text):
    ascii_list = []
    for char in text:
        ascii_list.append(ord(char))
    return ascii_list


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

    image_input_path = "./images/basketBall.png"
    image_output_path = ""
    encode_text = "Hello Oussama"

    encode(image_input_path, encode_text, image_output_path)


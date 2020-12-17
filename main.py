"""
Name : main.py.py
Author : OBR01
Contect : brich.oussama@gmail.com
Time    : 17/12/2020 16:16
Desc:
"""
import png


def encode(input_path, output_path):
    r = png.Reader(input_path)
    print(r.read()[2])
    for row in r.asRGB()[2]:
        print(list(row))

# def get_rgb_ordered(rgb_rows):


#################
# Main Function #
#################
if __name__ == "__main__":
    print("Staring...")
    image_input_path = "./images/basketBall.png"
    image_output_path = ""

    encode(image_input_path, image_output_path)


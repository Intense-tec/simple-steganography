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
    for row in r.asRGB()[2]:
        rgb_rows.append(list(row))
    # print(rgb_rows)
    # rgb_pixels_list = get_rgb_ordered(rgb_rows)

    ascii = convert_text_to_ascii("Hello Alice !")

    print(rgb_rows[0])
    for char in ascii:
        print(bin(char)[2:].zfill(8))

    '''
    Loop in ascii values of char
    and change the r/b/g value to even if binary is 1
    if not then change the r/b/g value to odd    
    '''
    pixel_rgb_position = 0
    row = 0
    column = 0

    for index, char_ascii in enumerate(ascii):
        char_binaries = bin(char_ascii)[2:].zfill(8)
        for binary in char_binaries:
            row = pixel_rgb_position // len(rgb_rows)
            column = pixel_rgb_position % len(rgb_rows)
            if binary == "0" and (rgb_rows[row][column] % 2) != 0:
                rgb_rows[row][column] = rgb_rows[row][column] - 1
            elif binary == "1" and (rgb_rows[row][column] % 2) == 0:
                rgb_rows[row][column] = rgb_rows[row][column] - 1
            pixel_rgb_position += 1

        '''
        Add separation sign : change r/g/b to odd (value-1) 
        '''
        row = pixel_rgb_position // len(rgb_rows)
        column = pixel_rgb_position % len(rgb_rows)
        if len(ascii) > index:
            if (rgb_rows[row][column] % 2) == 0:
                rgb_rows[row][column] = rgb_rows[row][column] - 1
        else:
            if (rgb_rows[row][column] % 2) != 0:
                rgb_rows[row][column] = rgb_rows[row][column] - 1
        pixel_rgb_position += 1

    print(rgb_rows[0])
    return rgb_rows


# Decode text from image
def decode(image_path, rgb_rows):
    text = ""
    binaries = []
    is_text_end = False

    for rgb_row in rgb_rows:
        binary = ""
        rgb_position = 0
        binary_count = 0

        # If end of text encrypted in image then break
        if is_text_end:
            break

        # Loop in r/g/b values
        for value in rgb_row:
            # If end of binary block (8 r/g/b values)
            if binary_count == 8:
                if (value % 2) == 0:
                    is_text_end = True
                    break
                else:
                    # Append char binary
                    binaries.append(binary)
                    binary = ""
                    binary_count = 0
                    # ignore separation
                    continue

            if (value % 2) == 0:
                binary += "0"
            else:
                binary += "1"

            binary_count += 1
    print(str(binaries))


# Convert text to ascii list
def convert_text_to_ascii(text):
    ascii_list = []
    for char in text:
        ascii_list.append(ord(char))
    return ascii_list


# Convert ascii list decoded to text
def convert_ascii_to_text(ascii_list):
    text = ""
    for ascii in ascii_list:
        text += chr(ascii)
    return text

# Order RGB list (as : [(R,G,B), (R,G,B), ...]
# def get_rgb_ordered(rgb_rows):
#     rgb_pixels_list = []
#     for row in rgb_rows:
#         rgb_pixels = [row[x:x + 3] for x in range(0, len(row), 3)]
#         rgb_pixels_list.append(rgb_pixels)
#     return rgb_pixels_list


#################
# Main Function #
#################
if __name__ == "__main__":

    image_input_path = "./images/basketBall.png"
    image_output_path = ""
    encode_text = "Hello Oussama"

    encoded_image = encode(image_input_path, encode_text, image_output_path)
    decode("", encoded_image)

"""
Name : main.py
Author : Oussama BRICH
Contact : brich.oussama@gmail.com
Time    : 17/12/2020 16:16
Desc: encode text in image
"""
import png
import argparse


def encode(input_path, text, output_path):
    """
    Encode text in input image and save it with the change
    :param input_path:  str
    :param text: ste
    :param output_path: str
    :return: output_path: str
    """

    rgb_rows = get_rgb_values_from_image(input_path)

    ascii = convert_text_to_ascii(text)

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

    rgb_rows = adapt_rgb_to_write(rgb_rows)
    save_output_image(output_path, rgb_rows)

    return output_path


def decode(image_path, rgb_rows):
    """
    Decode text from image
    :param image_path: str
    :param rgb_rows: str
    :return: text: str
    """
    binaries = []
    is_text_end = False

    rgb_rows = get_rgb_values_from_image(image_path)

    for rgb_row in rgb_rows:
        binary = ""
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

    # Get text value fom binaries
    ascii_list = []

    for binary in binaries:
        int_value = int(binary, 2)
        ascii_list.append(int_value)

    text = convert_ascii_to_text(ascii_list)

    return text


def convert_text_to_ascii(text):
    """
    Convert text to ascii list
    :param text: str
    :return ascii_list:  list
    """
    ascii_list = []
    for char in text:
        ascii_list.append(ord(char))
    return ascii_list


def get_rgb_values_from_image(image_path):
    """
    Get rgb value from image
    :param image_path: str
    :return: rgb_rows: list
    """

    rgb_rows = []

    r = png.Reader(image_path)
    for row in r.asRGB()[2]:
        rgb_rows.append(list(row))

    return rgb_rows


# Convert ascii list decoded to text
def convert_ascii_to_text(ascii_list):
    text = ""
    for ascii in ascii_list:
        text += chr(ascii)
    return text


def save_output_image(output_path, rgb_list):
    """
    Save output image from rgb list
    :param output_path: str
    :param rgb_list: list
    :return output_path: str
    """
    width = int(len(rgb_list[0])/3)
    high = len(rgb_list)

    f = open(output_path, 'wb')
    w = png.Writer(width, high, greyscale=False)
    w.write(f, rgb_list)
    f.close()
    return output_path


def adapt_rgb_to_write(rgb_rows):
    """
    Order RGB list (as : [(R,G,B, R,G,B R,G,B), (...), ...]
    :param rgb_rows: str
    :return rgb_pixels_list: list
    """
    rgb_pixels_list = []
    for row in rgb_rows:
        rgb_pixels = tuple(row)
        rgb_pixels_list.append(rgb_pixels)

    return rgb_pixels_list


#################
# Main Function #
#################
if __name__ == "__main__":
    # Image default output path
    image_output_path = "./images/image_with_message_encoded.png"

    # Parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", '--file', help='file input')
    parser.add_argument("-t", '--text', help='text to encode')
    args = parser.parse_args()

    if args.file:
        image_input_path = args.file
    if args.text:
        encode_text = args.text
    else:
        encode_text = "Hello human! this is a default toto text"

    encoded_image = encode(image_input_path, encode_text, image_output_path)
    print("Image with text encoded saved in : " + encoded_image)
    decoded_text = decode(encoded_image, encoded_image)
    print("Decoded text : " + decoded_text)

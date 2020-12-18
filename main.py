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


# Decode text from image
def decode(image_path, rgb_rows):
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


# Convert text to ascii list
def convert_text_to_ascii(text):
    ascii_list = []
    for char in text:
        ascii_list.append(ord(char))
    return ascii_list


# Get rgb value from image
def get_rgb_values_from_image(image_path):
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


# Save output image from rgb list
def save_output_image(output_path, rgb_list):
    width = int(len(rgb_list[0])/3)
    high = len(rgb_list)

    f = open(output_path, 'wb')
    w = png.Writer(width, high, greyscale=False)
    w.write(f, rgb_list)
    f.close()
    return output_path


# Order RGB list (as : [(R,G,B, R,G,B R,G,B), (...), ...]
def adapt_rgb_to_write(rgb_rows):
    rgb_pixels_list = []
    for row in rgb_rows:
        rgb_pixels = tuple(row)
        rgb_pixels_list.append(rgb_pixels)

    return rgb_pixels_list


#################
# Main Function #
#################
if __name__ == "__main__":

    image_input_path = "./images/image.png"
    image_output_path = "./images/image_with_message_encoded.png"
    encode_text = "Hello Oussama"

    encoded_image = encode(image_input_path, encode_text, image_output_path)
    print("Image with text encoded saved in : " + encoded_image)
    text = decode(encoded_image, encoded_image)
    print("Decoded text : " + text)

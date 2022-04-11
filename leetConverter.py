import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def leet_converter(text):
    char_mapping = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        't': '7',
        's': '5'
    }
    converted_text = ""
    for char in text:
        if char.lower() in char_mapping:
            converted_text += char_mapping[char.lower()]
        else:
            converted_text += char
    return converted_text


def main():
    # fetch file using a file browser, check validity of file
    Tk().withdraw()
    input_filename = askopenfilename()
    print(input_filename)
    if input_filename == '' or not os.path.splitext(input_filename)[1] == '.txt':
        print('no valid file selected')
        return

    input_file = open(input_filename, "r")
    if not input_file.readable():
        print('file selected is not readable')
        return

    # setup new text file to write the converted text
    input_path, input_name = os.path.split(input_file.name)
    converted_filename = input_path + "//" + os.path.splitext(input_name)[0] + "_1337converted.txt"
    converted_file = open(converted_filename, "x")

    # convert text
    new_text = leet_converter(input_file.read())
    converted_file.write(new_text)

    # close files
    input_file.close()
    converted_file.close()


if __name__ == '__main__':
    main()

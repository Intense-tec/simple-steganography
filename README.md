# simple-steganography 
The goal of this project is to produce a self-contained tool in Python that can be used for covert
messaging. The tool is able to “hide” ASCII text inside PNG files.

Launch with : python3 main.py
```console 
$ python3 main.py
```

Options :
- -f : image path used to encode text (format png RGB is required). If not specified
images/images.png will be the input per default.

command :
```console 
$ python3 main.py -f ./images/image.png
```

- -t :  text to encode in image. If not specified "Hello human!" will be the input per default.

command :
```console 
$ python3 main.py -f ./images/image.png -t "Alice and bob use this!"
```

- -h : Show help.

By Oussama BRICH (brich.oussama@gmail.com),
No constraints to use this code.
__
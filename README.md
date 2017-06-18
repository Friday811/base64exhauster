# Base64 String Finder

This python script finds 3 possible Base64 encodings of a given input string.
You can search for these 3 encodings in any base64 encoded block to find the input string without needing to decode the block.

Three encodings is the minimum amount required to identify all possible locations for the string.
There may be some false positives, but it should not miss any true occurences of the string. 
Avoiding false positives would require creating a larger list of longer strings. Perhaps I will add this functionality in the future.


### Usage
```
user@machine:~/base64exhauster$ chmod +x base64exhauster.py

user@machine:~/base64exhauster$ ./base64exhauster.py -h
usage: base64exhauster.py [-h] [--encoding ENCODING] sequence

positional arguments:
  sequence              The input sequence (minimum 3 characters) to display
                        all possible Base64 encodings.

optional arguments:
  -h, --help            show this help message and exit
  --encoding ENCODING, -e ENCODING
                        The encoding to be used for the string, default is
                        utf-8


user@machine:~/base64exhauster$ ./base64exhauster.py 'Hello, world!'
Your string: Hello, world!
Using encoding: utf-8
Binary sequence: 01001000 01100101 01101100 01101100 01101111 00101100 00100000 01110111 01101111 01110010 01101100 01100100 00100001 
Hex sequence: 0x48 0x65 0x6C 0x6C 0x6F 0x2C 0x20 0x77 0x6F 0x72 0x6C 0x64 0x21 
Number of bits: 104
Number of bytes: 13
First possibility: SGVsbG8sIHdvcmxkI
Second possibility: hlbGxvLCB3b3JsZC
Third possibility: IZWxsbywgd29ybGQh
```

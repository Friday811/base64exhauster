# Base64 String Finder

This python script finds 3 possible Base64 encodings of a given input string.
You can search for these 3 encodings in any base64 encoded block to find the input string without needing to decode the block.

Three encodings is the minimum amount required to identify all possible locations for the string.
There may be some false positives, but it should not miss any true occurences of the string. 
Avoiding false positives would require creating a larger list of longer strings. Perhaps I will add this functionality in the future.


### Usage
```
chmod +x base64exhauster.py
./base64exhauster.py [-h] [--encoding ENCODING] 'text sequence'
```

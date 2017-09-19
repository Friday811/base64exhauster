#!/usr/bin/env python3

import argparse
import base64

ENCODING = 'utf-8'

parser = argparse.ArgumentParser()
parser.add_argument("sequence", help="The input sequence (minimum 3"
                    " characters) to display all possible Base64"
                    " encodings.", type=str)
parser.add_argument("--encoding", "-e", help="The encoding to be used for the"
                    " string, default is utf-8", type=str)
args = parser.parse_args()

sequence = args.sequence
if args.encoding:
    ENCODING = args.encoding

if len(sequence) < 3:
    print("Error! Sequence must be at least 3 characters.")
    print("Use -h or --help for more information.")
else:
    print("Your string: " + sequence)
    print("Using encoding: " + ENCODING)
    data = bytes(sequence.encode(ENCODING))
    binary_sequence = ''
    hex_sequence = ''
    for byte in data:
        binary_sequence += format(byte, '08b') + ' '
    for byte in data:
        hex_sequence += '0x' + format(byte, 'X') + ' '
    print("Binary sequence: " + binary_sequence)
    print("Hex sequence: " + hex_sequence)
    # account for extra space betwen bytes
    num_bytes = len(binary_sequence)//9
    # multiply by 8 for bits
    num_bits = num_bytes*8
    print("Number of bits: " + str(num_bits))
    print("Number of bytes: " + str(num_bytes))
    b64_sequence_len = (num_bits-8)//6
    b64_sequence_bits = b64_sequence_len*6

    # First possible sequence starts with 2nd byte and creates
    # base64 sequence up until last byte is included but goes no further.
    padding = 3-((num_bytes) % 3)
    sequence_1 = str(base64.b64encode(data + bytes(padding)))[:-(padding+1)]
    sequence_1_bits = bytes(sequence_1.encode(ENCODING))
    print("First possibility: " + sequence_1[2:-1])

    # Second possible sequence includes last 2 bits of first byte
    padding = 2-(num_bytes % 3)
    if padding == 0:
        print("Second possibility: " +
              str(base64.b64encode(bytes(1) +
                                   data +
                                   bytes(padding))[2:])[2:-1])
    else:
        print("Second possibility: " +
              str(base64.b64encode(bytes(1) +
                                   data +
                                   bytes(padding))[2:-(padding+1)])[2:-1])

    # Third possible sequence includes last 4 bits of the first byte
    remainder = num_bytes % 3
    if remainder == 0:
        padding = 1
    elif remainder == 2:
        padding = 2
    elif remainder == 1:
        padding = 0
    else:
        print("ERROR!")
        sys.exit(1)
    if padding == 0:
        print("Third possibility: " +
              str(base64.b64encode(bytes(2) +
                                   data +
                                   bytes(padding))[3:])[2:-1])
    else:
        print("Third possibility: " +
              str(base64.b64encode(bytes(2) +
                                   data +
                                   bytes(padding))[3:-(padding+1)])[2:-1])

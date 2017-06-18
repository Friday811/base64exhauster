#!/usr/bin/env python3

import argparse
import base64

ENCODING = 'utf-8'

parser = argparse.ArgumentParser()
parser.add_argument("sequence", help="The input sequence (minimum 3 characters) to display all possible Base64 encodings.", type=str)
parser.add_argument("--encoding", "-e", help="The encoding to be used for the string, default is utf-8", type=str)
args = parser.parse_args()

sequence = args.sequence
if args.encoding:
    ENCODING = args.encoding

if len(sequence) < 3:
    print("Error! Sequence must be at least 3 characters.")
    print("Use -h or --help for more information.")
else:
    #num_bytes = len(sequence)
    #num_bits = num_bytes * 8
    print("Your string: " + sequence)
    #print("Number of bytes: " + str(num_bytes))
    #print("Number of bits: " + str(num_bits))
    print("Using encoding: " + ENCODING)
    #print("Binary sequence: ")
    data = bytes(sequence.encode(ENCODING))
    #for byte in data:
    #    print(format(byte, '08b'), end=" ")
    #print()
    
    binary_sequence = ''
    hex_sequence = ''
    for byte in data:
        binary_sequence += format(byte, '08b') + ' '
    for byte in data:
        hex_sequence += '0x' + format(byte, 'X') + ' '
    print("Binary sequence: " + binary_sequence)
    print("Hex sequence: " + hex_sequence)
    num_bytes = len(binary_sequence)//9 # account for extra space betwen bytes
    num_bits = num_bytes*8 # multiply by 8 for bits
    print("Number of bits: " + str(num_bits))
    print("Number of bytes: " + str(num_bytes))
    b64_sequence_len = (num_bits-8)//6
    b64_sequence_bits = b64_sequence_len*6
    #print("Base64 sequence length: " + str(b64_sequence_len))

    # First possible sequence starts with 2nd byte and creates base64 sequence up until last byte is included but goes no further.
    #sequence_1 = binary_sequence[:b64_sequence_bits]
    padding = 3-((num_bytes) % 3)
    #print("First sequence bits: " + sequence_1)
    #print(data[1:] + bytes(padding))
    sequence_1 = str(base64.b64encode(data + bytes(padding)))[:-(padding+1)]
    sequence_1_bits = bytes(sequence_1.encode(ENCODING))
    #print("First bits: ", end="")
    #for byte in sequence_1_bits:
    #    print(format(byte, '08b'), end='')
    #print()
    print("First possibility: " + sequence_1[2:-1])

    # Second possible sequence includes last 2 bits of first byte
    #sequence_2 = binary_sequence[6:6+b64_sequence_bits]
    #print("Second sequence bits: " + sequence_2)
    padding = 2-(num_bytes%3)
    #print(str(padding))
    if padding == 0:
        print("Second possibility: " + str(base64.b64encode(bytes(1) + data + bytes(padding))[2:])[2:-1])
    else:
        print("Second possibility: " + str(base64.b64encode(bytes(1) + data + bytes(padding))[2:-(padding+1)])[2:-1])


    # Third possible sequence includes last 4 bits of the first byte
    #sequence_3 = binary_sequence[4:4+b64_sequence_bits]
    #print("Third sequence bits: " + sequence_3)
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
    #print(str(padding))
    if padding == 0:
        print("Third possibility: " + str(base64.b64encode(bytes(2) + data + bytes(padding))[3:])[2:-1])
    else:
        print("Third possibility: " + str(base64.b64encode(bytes(2) + data + bytes(padding))[3:-(padding+1)])[2:-1])

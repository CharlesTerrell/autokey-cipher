#!/usr/bin/env python

# Author: Charles Terrell <tachyon@pobox.com>
# version 0.1.0
# Encrypt / decrypt using classic autokey ciphers

import re
from latin import Latin

class AutokeyCipher:
    def __init__(self, key_text, src_text):
        key_text = Latin.latinize(key_text)
        src_text = Latin.latinize(src_text)
        key_text = re.sub("[^a-zA-Z]", '', key_text).upper()
        src_text = re.sub("[^a-zA-Z]", '', src_text).upper()
        self.key = [ord(letter)-65 for letter in key_text]
        self.src = [ord(letter)-65 for letter in src_text]

    def encode(self):
        self.key = self.key + self.src
        new_values = [chr(65 + (self.src[idx] + self.key[idx]) % 26)
                      for idx in range(len(self.src))]
        return ''.join(new_values)

    def decode(self):
        for idx in range(len(self.src)):
            self.key.append((self.src[idx] - self.key[idx]) % 26)
        return ''.join([chr(65 + num) for num in self.key[-len(self.src):]])
    
def args():
    import argparse
    parser = argparse.ArgumentParser(description='Encodes and decodes using autokey cipher')
    parser.add_argument("-d", "--decode", dest='decode', action='store_true', help="decode message")
    parser.add_argument("-e", "--encode", dest='decode', action='store_false', help="encode message (default)")
    parser.add_argument("key", help="text for primer key")
    parser.add_argument("src", help="text to encode or decode")
    args = parser.parse_args()
    return vars(args)

def main():
    config = args()
    # print(config)
    key = config["key"]
    print("key: " + key)
    src = config["src"] 
    print("src: " + src)
    cipher = AutokeyCipher(key, src)
    result = ""
    if (config["decode"]):
        result = cipher.decode()
    else:
        result = cipher.encode()
    print("out: " + result)

if __name__ == "__main__":
    main()


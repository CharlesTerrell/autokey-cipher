# Autokey Cipher
Encrypt/decrypt using the classic cipher, with automatic character set conversion from extended Latin to plain ISO Latin. (The charset conversion is currently limited but can be expanded as needed.) During preparation for encryption it removes spaces, punctuation, and anything else that isn't a letter from both key and plaintext.

## About the cipher
Autokey cipher was state of the art encryption for hundreds of years. Now it's obsolete for serious secret-keeping, but it still has value for education and entertainment. The basic idea is to shift the alphabet of each letter in the plaintext by a different offset, starting with an initial "primer" key. The message itself is added to the end of the key to extend it to the right length.

These web sites explain it better:
* [https://en.wikipedia.org/wiki/Autokey_cipher](https://en.wikipedia.org/wiki/Autokey_cipher)
* [https://crypto.interactive-maths.com/autokey-cipher.html](https://crypto.interactive-maths.com/autokey-cipher.html)
* [http://www.practicalcryptography.com/ciphers/autokey-cipher/](http://www.practicalcryptography.com/ciphers/autokey-cipher/)

## Output of 'autokey.py --help'
    usage: autokey.py [-h] [-d] [-e] key src

    Encodes and decodes using autokey cipher

    positional arguments:
    key           text for primer key
    src           text to encode or decode

    options:
    -h, --help    show this help message and exit
    -d, --decode  decode message
    -e, --encode  encode message (default)

## examples
    autokey.py "boots" "Swiper, no swiping! Oh man..."
    key: boots
    src: Swiper, no swiping! Oh man...
    out: TKWIWJJWHAZCWFCWWUNT

    autokey.py -d "boots" "TKWIWJJWHAZCWFCWWUNT"
    key: boots
    src: TKWIWJJWHAZCWFCWWUNT
    out: SWIPERNOSWIPINGOHMAN

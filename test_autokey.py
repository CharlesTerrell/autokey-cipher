from autokey import AutokeyCipher

# "queenly" examples from wikipedia
# https://en.wikipedia.org/wiki/Autokey_cipher
def test_encode_queenly():
    cipher = AutokeyCipher("queenly", "attack at dawn")
    assert cipher.encode() == "QNXEPVYTWTWP"

def test_decode_queenly():
    cipher = AutokeyCipher("queenly", "qnxepvytwtwp")
    assert cipher.decode() == "ATTACKATDAWN"

# "corner" and "eastwall" examples from Crypto Corner
# https://crypto.interactive-maths.com/autokey-cipher.html
def test_encode_corner():
    cipher = AutokeyCipher("king", "meet me at the corner")
    assert cipher.encode() == "WMRZYIEMFLEVHYRGF"

def test_decode_corner():
    cipher = AutokeyCipher("king", "WMRZYIEMFLEVHYRGF")
    assert cipher.decode() == "MEETMEATTHECORNER"

def test_encode_eastwall():
    cipher = AutokeyCipher("queen", "attack the east wall at dawn")
    assert cipher.encode() == "QNXEPKMAEGKLAAELDTPDLHN"

def test_decode_eastwall():
    cipher = AutokeyCipher("queen", "QNXEPKMAEGKLAAELDTPDLHN")
    assert cipher.decode() == "ATTACKTHEEASTWALLATDAWN"

def test_encode_esperanto():
    cipher = AutokeyCipher("tute ne gravas", "Eĥoŝanĝo ĉiuĵaŭde kaj ĉiudimanĉe")
    assert cipher.encode() == "XBQSFBGEGSOUBPRXPXUKJBYCGKRRRDCJDRMXN"

def test_decode_esperanto():
    cipher = AutokeyCipher("tute ne gravas", "XBQSFBGEGSOUBPRXPXUKJBYCGKRRRDCJDRMXN")
    assert cipher.decode() == "EHXOSXANGXOCXIUJXAUXDEKAJCXIUDIMANCXE"


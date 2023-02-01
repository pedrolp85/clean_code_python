class Cipher:
    DECODE_BASE = "decode-"
    ENCODE_BASE = "encode-"

    def __init__(self, map1, map2):
        self.dictionary = {}
        for e, d in zip(map1, map2):
            self.dictionary[f"{self.ENCODE_BASE}{e}"] = d
            self.dictionary[f"{self.DECODE_BASE}{d}"] = e

    def _translate(self, base: str, text: str) -> str:
        encoded_string = ""
        for char in text:
            encoded_string += self.dictionary[f"{base}{char}"]
        return encoded_string

    def encode(self, s):
        return self._translate(self.ENCODE_BASE, s)

    def decode(self, s):
        return self._translate(self.DECODE_BASE, s)


"""
map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";
"""

cif = Cipher("abcdefghijklmnopqrstuvwxyz", "etaoinshrdlucmfwypvbgkjqxz")
print(cif.dictionary)


print(cif.decode(cif.encode("hola")))

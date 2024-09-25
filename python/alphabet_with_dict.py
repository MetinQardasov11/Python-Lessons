import string
import pprint

print(string.ascii_lowercase)
print(string.ascii_uppercase)

upper_az = ('A', 'B', 'C', 'Ç', 'D', 'E', 'Ə', 'F', 'G', 'Ğ', 'H', 'X', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z')

lower_az = ('a', 'b', 'c', 'ç', 'd', 'e', 'ə', 'f', 'g', 'h', 'x', 'i', 'ı', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's', 'ç', 't', 'u', 'ü', 'v', 'y', 'z')

alphabet = {lo: up for lo, up in zip(lower_az, upper_az)}
print(alphabet)

pprint.pprint(alphabet, sort_dicts=False)
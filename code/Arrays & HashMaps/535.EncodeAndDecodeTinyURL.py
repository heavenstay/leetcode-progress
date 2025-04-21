# Problem: Encode And Decode Tiny URL: https://leetcode.com/problems/encode-and-decode-tinyurl/
# Difficulty: Medium
# Time Taken: 8 min
# Attempts: 1
# Hints Used: No
# Notes: Use a dictionnary to store the correspondance between the encoded key and the long url. This code can be improve by adding an other hash_map to verify if the url hasn't already encoded, and by verifying if the key wasn't already used even tough the probability is very low. 
class Codec:
    def __init__(self):
        self.__map_encoding_urls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        uniqueEncodedKey = generate_random_key()
        self.__map_encoding_urls[uniqueEncodedKey] = longUrl
        return "http://tinyurl.com/" + uniqueEncodedKey

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        uniqueEncodedKey = shortUrl.split("http://tinyurl.com/")[1]
        return self.__map_encoding_urls[uniqueEncodedKey]

def generate_random_key():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))
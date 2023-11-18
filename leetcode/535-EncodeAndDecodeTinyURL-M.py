import random
import string


class Codec:

    def __init__(self):
        self.encodeURL = {}
        self.decodeURL = {}
        self.encryptionKeyDB = {}
        self.baseTinyURL = "http://tinyurl.com/"
        self.charDigit = string.ascii_letters + string.digits
    
    def getEncryptionKey(self):
        encryptionKey = ''.join(random.choice(self.charDigit) for i in range(6))
        return encryptionKey

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeURL:
            encryptionKey = self.getEncryptionKey()
            if encryptionKey in self.encryptionKeyDB: encryptionKey = self.getEncryptionKey() 
            tinyURL = self.baseTinyURL + encryptionKey
            self.encodeURL[longUrl] = tinyURL
            self.decodeURL[tinyURL] = longUrl 
        return self.encodeURL[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeURL[shortUrl]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
ExpectedOutput = "https://leetcode.com/problems/design-tinyurl"
encodedURL = codec.encode(url)
Output = codec.decode(encodedURL) 
print("\nEncoded Url is: ", encodedURL)
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(1)\n" )

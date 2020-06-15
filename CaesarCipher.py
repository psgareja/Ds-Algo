class CaesarCiphar:
    def __init__(self,shift):
        encoder=[None]*26
        decoder=[None]*26
        for k in range(26):
            encoder[k]=chr((k+shift)%26+ord('A'))
            decoder[k]=chr((k-shift)%26+ord('A'))
            self._forward=''.join(encoder)
            self._backward=''.join(decoder)
    def encrypt(self,message):
        return self.transform(message,self._forward)

    def decrypt(self,secret):
        return self.transform(secret,self._backward)

    def transform(self,original ,code):
        msg=list(original)
        for k in range(len(message)):
            if msg[k].isupper():
                j=ord(msg[k]-ord('A'))
                msg[k]=code[j]
        return ''.join(msg)

if __name__=='__main__':
    cipher=CaesarCiphar(3)
    message="pradip is always learning ."
    coded=cipher.encrypt(message)
    print('SEcret',coded)
    answer=decrypt(coded)
    print('Message ',answer)
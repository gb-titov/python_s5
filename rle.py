
class RLE:
    
    def encrypt(text):
        chr = text[0]
        enc_str = ''
        counter = 1
        for c in range(1, len(text)):
            if text[c] == chr:
                counter +=1
                continue
            enc_str+=str(counter)
            enc_str+=str(chr)
            chr = text[c]
            counter = 1
        enc_str+=str(counter)
        enc_str+=chr
        
        return enc_str

    def decrypt(text):
        new_str = ''
        count = ''
        for c in text:
            if c.isdigit():
                count += c
                continue
            new_str += c * int(count)
            count = ''
        return new_str

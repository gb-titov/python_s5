
class RLE:
    
    def encrypt(text):
        chr = text[0]
        enc_str = ''
        counter = 1
        for c in text:
            if c == chr:
                counter +=1
                continue
            enc_str+=str(counter)
            enc_str+=str(chr)
            chr = c
            counter = 1
        enc_str+=str(counter)
        enc_str+=chr
        
        return enc_str

    def decrypt(text):
        new_str = ''
        count = 0
        for c in text:
            if c.isdigit():
                count = int(c)
                continue
            new_str+=c*count
            count = 0
        return new_str

    

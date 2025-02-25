sentence = input("Çevirmek istediğiniz cümleyi giriniz: ")

mapping = {
        'a': '𐰆', 'b': '𐰊', 'c': '𐰌', 'ç': '𐰍', 'd': '𐰏', 'e': '𐰖', 'f': '𐰗', 'g': '𐰘',
        'h': '𐰚', 'ı': '𐰝', 'i': '𐰝', 'j': '𐰞', 'k': '𐰟', 'l': '𐰠', 'm': '𐰡', 'n': '𐰢',
        'o': '𐰣', 'ö': '𐰤', 'p': '𐰥', 'r': '𐰦', 's': '𐰧', 'ş': '𐰨', 't': '𐰩', 'u': '𐰪',
        'ü': '𐰫', 'v': '𐰬', 'y': '𐰭', 'z': '𐰮',' ':' '
    }

# bu aslında sonuç stringi olacak
converted = ""
#cümlenin içindeki harfleri teker teker arıyoruz
for char in sentence:
    # eğer harf göktürk alfabesinde mevcutsa
    if char in mapping:
        # o harfin göktürk karşılığını stringe ekliyoruz
        converted += mapping[char]
    #eğer mevcut değilse latin alfabesi ile ekliyoruz
    else:
        converted += char

# sonucu yazdırıyoruz
print(converted)
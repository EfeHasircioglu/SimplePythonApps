""" ilk olarak bir oyun tahtası olacak. oyun kordinat sistemi ile çalışsın. oyun 3x3 bir tahtada, eğer o'lar ya da x'ler dikey, yatat yada çapraz bir şekilde yer alırsa oyun bitecek """
print("Hoş geldiniz!")
def print_grid():
    for i in range(3):
        row = " | ".join(grid[i*3:(i+1)*3])  # Format each row
        print(row)
        if i < 2:
            print("-" * 9)  # Add a horizontal line between rows
hamlesayisi = 0
grid = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
print_grid()



def xOyuncusu():
    global hamlesayisi
    inp = input("X oyuncusu oynuyor.\nNereye hamle yapmak istersiniz? ")
    inp = int(inp)
    adj_inp = inp - 1
    if grid[adj_inp] == "_":
        grid[adj_inp] = "X"
        print_grid()
        hamlesayisi += 1
    else:
        print("Oynamak istedğiniz yerde zaten oynanmış.")
   

def Ooyuncusu():
    global hamlesayisi
    inp = input("O oyuncusu oynuyor.\nNereye hamle yapmak istersiniz? ")
    inp = int(inp)
    adj_inp = inp - 1
    if grid[adj_inp] == "_":
        grid[adj_inp] = "O"
        print_grid()
        hamlesayisi += 1
    else:
        print("Oynamak istedğiniz yerde zaten oynanmış.")
   

def bittiMi():
    kazandiran_kombinasyonlar = [
        # Rows
        [grid[0], grid[1], grid[2]],
        [grid[3], grid[4], grid[5]],
        [grid[6], grid[7], grid[8]],
        # Columns
        [grid[0], grid[3], grid[6]],
        [grid[1], grid[4], grid[7]],
        [grid[2], grid[5], grid[8]],
        # Diagonals
        [grid[0], grid[4], grid[8]],
        [grid[2], grid[4], grid[6]],
    ]
    
    for cmb in kazandiran_kombinasyonlar:
        if cmb == ["X", "X", "X"]:
            print("X kazandı!")
            return True
        elif cmb == ["O", "O", "O"]:
            print("O kazandı!")
            return True
        elif hamlesayisi == 9:
            print("Berabere!")
            return True
    return False

while (True):
    try:
        if bittiMi():
            break
        else:
            if hamlesayisi % 2 == 0:
                bittiMi()                
                xOyuncusu()
            elif hamlesayisi % 2 != 0:
                bittiMi()
                Ooyuncusu()
    except ValueError as e:
        print("Geçersiz değer!")


def reverse_compile():
    print("not made this yet")
    binary_dict = {
        "a": "01100001-", "b": "01100010-", "c": "01100011-", "d": "01100100-",
        "e": "01100101-", "f": "01100110-", "g": "01100111-", "h": "01101000-",
        "i": "01101001-", "j": "01101010-", "k": "01101011-", "l": "01101100-",
        "m": "01101101-", "n": "01101110-", "o": "01101111-", "p": "01110000-",
        "q": "01110001-", "r": "01110010-", "s": "01110011-", "t": "01110100-",
        "u": "01110101-", "v": "01110110-", "w": "01110111-", "x": "01111000-",
        "y": "01111001-", "z": "01111010-", " ": "00100000-", "\"": "00100010-",
        "(": "00101000-", ")": "00101001-", ":": "00111010-", ",": "00101100-",
        "=": "00111101-", "+": "00101011-", "*": "00101010-", "0": "00110000-",
        "1": "00110001-", "2": "00110010-", "3": "00110011-", "4": "00110100-",
        "5": "00110101-", "6": "00110110-", "7": "00110111-", "8": "00111000-",
        "9": "00111001-", "`": "01100000-", "'": "00100111-", ".": "00101110-",
        "/": "00101111-", "_": "01011111-", "%": "00100101-", "$": "00100100-",
        "[": "00111011-", "<": "00111100-", ">": "00111110-", "?": "00111111-",
        "A": "01000001-", "B": "01000010-", "C": "01000011-", "D": "01000100-",
        "E": "01000101-", "F": "01000110-", "G": "01000111-", "H": "01001000-",
        "I": "01001001-", "J": "01001010-", "K": "01001011-", "L": "01001100-",
        "M": "01001101-", "N": "01001110-", "O": "01001111-", "P": "01010000-",
        "Q": "01010001-", "R": "01010010-", "S": "01010011-", "T": "01010100-",
        "U": "01010101-", "V": "01010110-", "W": "01010111-", "X": "01011000-",
        "Y": "01011001-", "Z": "01011010-", "\n": "00001010-", "{": "01111011-",
        "}": "01111101-"
    }
    input("enter your python code\npress enter for enter\na single line with only exit is submit")
    code_orginal =  ""
    while True:
        line = input()

        if line == "exit":
            break
        else:
            code_orginal += line+"\n"
    print("this is your code:\n\n"+code_orginal)
    
    new_code = ""
    lines = code_orginal.split("\n")
    for line in lines:
        binary_line = ""
        for caractr in line:
            if caractr in binary_dict:
                binary_line += binary_dict[caractr]
            else:
                print(f"not found'{caractr}'")
                binary_line += caractr
        print(binary_line)
        new_code += binary_line + "\n"
    print(f"new_code:\n{new_code}")




def compile(file_Path):
    with open(file_Path, 'r') as file:
        data_Not_Done_1 = file.read()

    # Dictionary met correcte ASCII-waarden
    binary_dict = {
        "01100001-": "a", "01100010-": "b", "01100011-": "c", "01100100-": "d",
        "01100101-": "e", "01100110-": "f", "01100111-": "g", "01101000-": "h",
        "01101001-": "i", "01101010-": "j", "01101011-": "k", "01101100-": "l",
        "01101101-": "m", "01101110-": "n", "01101111-": "o", "01110000-": "p",
        "01110001-": "q", "01110010-": "r", "01110011-": "s", "01110100-": "t",
        "01110101-": "u", "01110110-": "v", "01110111-": "w", "01111000-": "x",
        "01111001-": "y", "01111010-": "z", "00100000-": " ", "00100010-": "\"",
        "00101000-": "(", "00101001-": ")", "00111010-": ":", "00101100-": ",",
        "00111101-": "=", "00101011-": "+", "00101010-": "*", "00110000-": "0",
        "00110001-": "1", "00110010-": "2", "00110011-": "3", "00110100-": "4",
        "00110101-": "5", "00110110-": "6", "00110111-": "7", "00111000-": "8",
        "00111001-": "9", "01100000-": "`", "00100111-": "'", "00101110-": ".",
        "00101111-": "/", "01011111-": "_", "00100101-": "%", "00100100-": "$",
        "00111011-": "[", "00111100-": "<", "00111110-": ">", "00111111-": "?",
        "01000001-": "A", "01000010-": "B", "01000011-": "C", "01000100-": "D",
        "01000101-": "E", "01000110-": "F", "01000111-": "G", "01001000-": "H",
        "01001001-": "I", "01001010-": "J", "01001011-": "K", "01001100-": "L",
        "01001101-": "M", "01001110-": "N", "01001111-": "O", "01010000-": "P",
        "01010001-": "Q", "01010010-": "R", "01010011-": "S", "01010100-": "T",
        "01010101-": "U", "01010110-": "V", "01010111-": "W", "01011000-": "X",
        "01011001-": "Y", "01011010-": "Z","00001010-":"\n","01111011-":"{",
        "01111101-":"}"
    }

    # Decodeer de binaire tekst
    for bin_val, char in binary_dict.items():
        data_Not_Done_1 = data_Not_Done_1.replace(bin_val, char)

    print("✅ Gecompileerde code:\n", data_Not_Done_1)
    return data_Not_Done_1


def main():
    which = input("compile and run: 1\nget binair code: 2")
    if which == "1":
        file_Path = input("Geef het pad naar het bestand: ")
        data = compile(file_Path)
        print("××××××××××××××××")
        exec(data)  # Voert de code uit
    elif which == "2":
        reverse_compile()

if __name__ == "__main__":
    main()

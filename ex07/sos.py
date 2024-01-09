import sys

def checkArgument(string : str) -> bool:
    splitted_data = string.split(' ')
    for i in splitted_data:
        if i.isalnum() == False:
            return False
    return True

def createMorseCodeData() -> dict:
    morse_code = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                  'S': '...', 'T': '-', 'U': '..-', 'V': '...-.', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                  '9': '----.', '0': '-----', ' ': '/' }
    return morse_code

def translateToMorseCode(morse_code: dict, args: str) -> str:
    results = ''
    for i in args:
        if i.isalpha() == True:
            results += morse_code[i.upper()]
        else:
            results += morse_code[i]
        results += ' '
    return results

def main():
    assert len(sys.argv) == 2, "the arguments are bad"
    assert checkArgument(sys.argv[1]) == True, "the arguments are bad"
    morse_codes = createMorseCodeData()
    results = translateToMorseCode(morse_codes, sys.argv[1])
    print(results)

if __name__ == "__main__":
    main()
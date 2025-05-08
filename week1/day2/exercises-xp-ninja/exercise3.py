
    
morse_to_english = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',

    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',

    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'",
    '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
    '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
    '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
    '...-..-': '$', '.--.-.': '@', '/': ' ' 
}
def get_key(val):
    for key, value in morse_to_english.items():
        if value == val:
            return key
    return None
def to_morse_code():
    while True:
        message = input("Enter the english message: ")
        for x in message:
            print(get_key(x.upper()),end="|")
        replay = input("\nDo you want to continue? (yes/no): ")
        if replay.lower() != "yes":
            break

def to_english_code():
    while True:
        message = input("Enter the morse code(split by '|' ): ")
        message = message.split("|")
        for x in message:
            print(morse_to_english[x],end="")
        replay = input("\nDo you want to continue? (yes/no): ")
        if replay.lower() != "yes":
            break

        
to_morse_code()
to_english_code()
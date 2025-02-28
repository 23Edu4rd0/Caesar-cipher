from encode_decode import EncodeDecode
from restart_game import Restart

class Game():
    def __init__(self):
        self.should_continue = True
        self.cipher = EncodeDecode()
        self.restart = Restart()

    
    def start(self):
        while self.should_continue:
            
            action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            
            message = input("Type your message:\n").lower()
            # Shift in caesar-cipher is the number of letters that will go up or down. 
            # Ex: number = 5, letter = a will become e
            shift_value = int(input("Type the shift number:\n"))
            
            self.cipher.caesar(message, shift_value, action)
            
            
            self.should_continue = self.restart.RestartGame()
                

        print("Goodbye")
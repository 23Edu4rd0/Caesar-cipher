from data import alphabet


class EncodeDecode:
    def __init__(self):
        self.alphabet = alphabet
        
        
    def caesar(self, original_text, shift_amount, encode_or_decode):
        output_text = ""
        
        for letter in original_text:
            if letter == ' ':
                output_text += letter
            elif letter in self.alphabet:
                if encode_or_decode == "decode":
                    shift_amount *= -1
                shifted_position = (self.alphabet.index(letter) + shift_amount) % len(self.alphabet)
                output_text += self.alphabet[shifted_position]
            else:  
                output_text += letter

        print(f"Here is the {encode_or_decode}d result: {output_text}")
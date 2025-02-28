
class Restart:
    def RestartGame(self):
        restart = input("Do you wanna continue? Type 'yes' or 'no' ").lower()
        if restart == "no":
            return False
        return True



class InvalidUserExcpetion(Exception):
    def __init__(self, message="You have not the rights to do this!"):
        self.message = message
        super().__init__(self.message)
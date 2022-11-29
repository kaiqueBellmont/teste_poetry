class Exceptions(Exception):
    def __init__(self, message=''):
        self.message = message
        super().__init__(message)

    def type_error_exception(self):
        self.message = f'Erro de tipo no valor {self}'
        return self.message, TypeError

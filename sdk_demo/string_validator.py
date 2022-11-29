class SimpleStringValidator:
    @staticmethod
    def simple_string_validator(value):
        if not isinstance(value, str):
            raise TypeError
        return True



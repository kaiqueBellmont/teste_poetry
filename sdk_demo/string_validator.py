class SimpleStringValidator:
    def simple_string_validator(self, value):
        if not isinstance(value, str):
            raise TypeError
        return True



class SimpleStringValidator:
    def simple_string_validator(self):
        if not isinstance(self, str):
            raise TypeError
        return True



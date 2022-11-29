class SimpleStringValidator:
    def simple_string_validator(self, value):
        try:
            if not isinstance(value, str):
                raise f'O valor {value} não pertence a classe str'
        except:
            if isinstance(value, str):
                return True


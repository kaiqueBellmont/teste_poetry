class SimpleStringValidator:
    def simple_comparation(self, value1, value2):
        try:
            if value1 > value2:
                return True
            return False
        except TypeError:
            raise ValueError("Erro de comparação entre tipos")
        finally:
            return False
    @staticmethod
    def ryan():
        print("Ryan de outro repositorio")

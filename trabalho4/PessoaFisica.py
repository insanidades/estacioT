from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, numeroConta, dataAberturaConta, status, dataNascimento, cpf, rg):
        super().__init__(nome, numeroConta, dataAberturaConta, status)
        self.__dataNascimento = dataNascimento
        self.__cpf = cpf
        self.__rg = rg

# Getters e Setters <3
    @property
    def dataNascimento(self):
        return self.__dataNascimento

    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) != 14:
            raise ValueError("O CPF deve conter 14 caracteres (no formato 000.000.000-00).")
        self.__cpf = cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg

    def imprimir_valores(self):
        return (super().imprimir_valores() + f", Data de Nascimento: {self.__dataNascimento}, "
                f"CPF: {self.__cpf}, RG: {self.__rg}")
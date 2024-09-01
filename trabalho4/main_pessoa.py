from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa = Pessoa("Carlos Silva", "54321", "2022-02-01", True)
print('Instância da classe Pessoa: ')
print(pessoa.imprimir_valores())

pessoa_fisica = PessoaFisica("Ana Souza", "67890", "2023-03-01", False, "1990-04-01", "000.111.222-33", "MG-12.345.678")
print('\nInstância da classe PessoaFisica: ')
print(pessoa_fisica.imprimir_valores())

pessoa_juridica = PessoaJuridica("Empresa XYZ", "98765", "2023-04-01", True, "2022-05-01", "00.000.000/0001-00")
print('\nInstância da classe PessoaJuridica: ')
print(pessoa_juridica.imprimir_valores())
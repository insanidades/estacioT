meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}

print(f'\nConteúdo do dicionário: \n{meu_dicionario}')

print(f'\nTipo de dados do dicionário: \n{type(meu_dicionario)}')

valor_linguagem = meu_dicionario.get(1)
print(f'\nValor da chave 1 no dicionário: \n{valor_linguagem}')

print(f'\nTamanho do dicionário: \n{len(meu_dicionario)}')

dicionario_frutas = dict({
    1: {'nome': 'limão', 'tipo': 'ácida'},
    2: {'nome': 'laranja', 'tipo': 'ácida'},
    3: {'nome': 'manga', 'tipo': 'semiácida'},
    4: {'nome': 'maçã', 'tipo': 'semiácida'},
    5: {'nome': 'banana', 'tipo': 'doce'},
    6: {'nome': 'mamão', 'tipo': 'doce'}
})

fruta1 = dicionario_frutas.get(1)
print('\nValores da chave 1:')
print(f'Nome: {fruta1.get('nome')}, Tipo: {fruta1.get('tipo')}')

fruta2 = dicionario_frutas.get(2)
print("\nValores da chave 2:")
print(f"Nome: {fruta2.get('nome')}, Tipo: {fruta2.get('tipo')}")

print('\nValores de todas as chaves de "nome" e "tipo":')
for chave, info in dicionario_frutas.items():
    print(f'Chave: {chave}, Nome: {info['nome']}, Tipo: {info['tipo']}')

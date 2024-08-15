set_inicial = {11, 12, 13, 14}

print(f'Conteúdo do set inicial: {set_inicial}')


set_inicial.add(15)
print(f'Após adicionar o elemento 15: {set_inicial}')

set_inicial.update({1, 2, 3, 4, 5})
print(f'Após atualizar o set inicial: {set_inicial}')

set_inicial.discard(13)
print(f'Após descartar o elemento 13: {set_inicial}')

novo_set = {20, 21, 23, 1, 2}
print(f'Conteúdo do novo set: {novo_set}')

uniao = set_inicial.union(novo_set)
print(f'Resultado da união entre o primeiro set e novo set: {uniao}')

intersec = set_inicial.intersection(novo_set)
print(f'Resultado da interseção entre o primeiro set e novo set: {intersec}')

diff = set_inicial.difference(novo_set)
print(f'Resultado da diferença entre o primeiro set e o novo set: {diff}')

diff_sim = set_inicial.symmetric_difference(novo_set)
print(f'Resultado da diferença simétrica entre o primeiro set e o novo set: {diff_sim}')
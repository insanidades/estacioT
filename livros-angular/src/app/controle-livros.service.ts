import { Injectable } from '@angular/core';
import { Livro } from './livro';

@Injectable({
  providedIn: 'root'
})
export class ControleLivrosService {
  private livros: Array<Livro> = [
    {
      codigo: 1,
      codEditora: 1,
      titulo: 'Oyasumi Punpun',
      resumo: 'Boa Noite Punpun é uma série de mangá escrita e ilustrada por Inio Asano sobre Onodera Punpun, uma criança normal representada na forma de um pássaro.',
      autores: ['Inio Asano']
    },
    {
      codigo: 2,
      codEditora: 2,
      titulo: 'Use a Cabeça: Java',
      resumo: 'Use a cabeça! Java é uma experiência completa de aprendizado em programação orientada a objetos',
      autores: ['Bert Bates', 'Kathy Sierra']
    },
    {
      codigo: 3,
      codEditora: 3,
      titulo: 'Java, como Programar',
      resumo: 'Milhões de alunos e profissionais aprendem programação e desenvolvimento de software com os livros Deitel',
      autores: ['Paul Deitel', 'Harvey Deitel']
    }
  ]

  obterLivros(): Array<Livro> {
  return this.livros;
  }

  incluir(novoLivro: Livro): void{
    let maiorcodigo = 0;

    for (let l of this.livros) {
      if (l.codigo > maiorcodigo) {
        maiorcodigo = l.codigo;
     }
    }
    novoLivro.codigo = maiorcodigo + 1;
    this.livros.push(novoLivro);
  }

  excluir(codigo: number): string {
    const indice = this.livros.findIndex(l => l.codigo === codigo); 
    if (indice !== -1) {
      this.livros.splice(indice, 1);
      return 'Livro excluído com sucesso';
    }
    return 'Livro não encontrado'; 
  }

  constructor() { }
}

/*
Eu quero que você crire neste exercicio um objeto de postagem de blog
que vai conter as seguintes propridades:
Postagem
Titulo
mensagem 
autor
visualizações
comentários
(autor,mensagem)
estaAoVivo
*/




/*
function Postagem(titulo, mensagem, autor, visualizacoes, comentarios){
  this.titulo = titulo;
  this.mensagem = mensagem;
  this.autor = autor;
  this.visualizações = visualizacoes;
  this.comentarios = comentarios;
}


const minhaPostagem = new Postagem('A importância da IA', 'doideira demais', 'David', 983289283, 'ok, show!');
console.log(minhaPostagem);
*/

/*
Eu quero que você crire neste exercicio um objeto de postagem de blog
que vai conter as seguintes propridades:
Postagem
Titulo
mensagem 
autor
visualizações
comentários
(autor,mensagem)
estaAoVivo

*/


let postagem = {
    titulo: 'a',
    mensagem: 'b',
    autor: 'c',
    visualizações: 10,
    comentarios: [
        {autor: 'a',mensagem: 'b'},
        {autor: 'a',mensgem: 'b'}
    ],
    estaAoVivo: true
}

console.log(postagem)
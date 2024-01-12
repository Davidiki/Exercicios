//Criar um método para ler propriedade de um objeto e exiber somente propridades do tipo string que estão nesse objeto
const filme={
    titulo: 'Vingadores',
    ano: 2018,
    diretor:'Robin',
    personagem: 'Thor'
}
mostraString(filme)
function mostraString(obj){
    for (let valor in filme) {
      if (typeof filme[valor] == 'string') {
        console.log(valor, filme[valor])  
      }
      
    }
}




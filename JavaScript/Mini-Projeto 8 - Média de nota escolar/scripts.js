/* Exercicio nota escolar
Obter a média a partir de um array

0-59: F
60-69: D
70-79: C
80-89: D
90-100: A
*/


const array = [70,70,80];
console.log(mediaDoAluno(array))

function mediaDoAluno(notas) {
  let soma = 0
  for (let i = 0; i <= array.length - 1; i++){
    soma += array[i]
  }
  let media = (soma / array.length)
  if(media < 60){
    return 'F'
  }if(60 <= media <= 69) {
    return 'D'
  }if(70 <= media <= 79){
    return 'C'
  }if(80 <= media <= 89){
    return 'B'
  }if(90 <= media <= 100){
    return 'A'
  }
}
// Operadores Aritméticos
/*let salario = 100

// + - * / **

console.log(salario + salario)
console.log(salario - salario)
console.log(salario * salario)
console.log(salario / salario)
console.log(5 ** 5)

  
let idade = 18

// ++:adiciona 1
console.log(idade++)
console.log(idade)

//-- Subtrai 1
console.log(idade--)
console.log(idade)


//Atribuição

let valorTecladoGamer = 100
valorTecladoGamer += valorTecladoGamer
console.log(valorTecladoGamer)

//Operadores de Igualdade

//Igualdade estrita
console.log(1 === 1)
console.log('1' === 1)

//Igualdade Solta
console.log(1 == 1)

//Operador Ternário
let pontos = 100
let tipo = pontos > 100 ? 'premium': 'comum'
console.log(tipo)

// Operadores lógicos e (&&)
// Retorna TRUE se os dois operadores forem true
console.log(false && true)


let maiorDeIdade = true;
let possuiCarteiraDeTrabalho = true
let podeAplicar = maiorDeIdade && possuiCarteiraDeTrabalho
console.log(podeAplicar)
*/
//Operador lógico ou(||)
//Retornar ture se um dos oprandos forem true
let maiorDeIdade = false
let possuiCarteiraDeTrabalho = false
let podeAplicar = maiorDeIdade || possuiCarteiraDeTrabalho
console.log(podeAplicar)

//Operador NOT(!)
let candidatoRecusado = !podeAplicar

console.log('Candidato Recusado', candidatoRecusado)

//Comparação não booleanos

// Falsy:
//undefined
//null
//0
//false
//''
//NaN = note a number

//Truthy:

let corPersonalizada = 'Vermelho'
let corPadrao = 'Azul';
let corPerfil = corPersonalizada || corPadrao

console.log(corPerfil)
// Add novos elementos
const numeros = [1,2,3];

// Inicio
numeros.unshift(0);
console.log(numeros);

// Meio
numeros.splice(1, 0, 'a');
console.log(numeros);

// Final
numeros.push(5);
console.log(numeros);

// Encontrando Elementos

// Tipos primitivos
const numeros2 = [1,2,3,4];
console.log(numeros2.indexOf(2));
console.log(numeros2.lastIndexOf(1));
console.log(numeros2.indexOf(2) !== -1);
console.log(numeros2.includes(2));

// Tipos de referência
const marcas = [
    {id: 1, nome: 'a'},
    {id: 2, nome: 'b'}
];

console.log(marcas.includes({id: 1, nome: 'a'}));

const marcaEncontrada = marcas.find(marca => marca.nome === 'a');
console.log(marcaEncontrada);

// Remover elementos
const numeros3 = [1,2,3,4,5,6];

// Inicio da Array
const primeiro = numeros3.shift();
console.log(primeiro);
console.log(numeros3);

// Meio
const meio = numeros3.splice(2, 1);
console.log(meio);

// Final
const ultimo = numeros3.pop();
console.log(ultimo);
console.log(numeros3);

// Esvaziando uma Array
let numeros4 = [1,2,3,4,5,6];
let outros = numeros4;

// Solução 1
numeros4 = [];
console.log(outros);

// Solução 2
numeros4.length = 0;
console.log(numeros4);
console.log(outros);

// Solução 3
numeros4.splice(0, numeros4.length);
console.log(numeros4);
console.log(outros);

// Solução 4
while (numeros4.length > 0) {
    numeros4.pop();
}



// Combinar elementos
const primeiro2 = [1, 2, 3];
const segundo2 = [4, 5, 6];
const combinado = primeiro2.concat(segundo2);
console.log(combinado);

// Dividir elementos
const cortado = combinado.slice(1);
console.log(cortado);

// Dividir com Spread
const primeiro3 = [1, 2, 3];
const segundo3 = [4, 5, 6];
const combinado2 = [...primeiro3, 'a', ...segundo3, '#'];
console.log(combinado2);
const clonado = [...combinado2];
console.log(clonado);

// Foreach
const numeros5 = [1, 2, 3, 4, 5];
numeros5.forEach((numero, indice) => console.log(numero, indice));

// Combinando Arrays
const numeros6 = [1, 2, 3, 4, 5];
const combinado3 = numeros6.join('-');
console.log(combinado3);

const frase = "olá bem vindo ao curso";
const resultado = frase.split(' ');
console.log(resultado);

console.log(resultado.join('-'));


//Escreva uma função que usa 2 números e retorna o maior entre eles

function maiorNumero(a, b) {
    if( a > b) {
        return a
    } else {
        return b
    }
}

console.log(maiorNumero(100,250))


let valorMaior = max(10,10)
console.log(valorMaior)

function max(numero1, numero2) {
    return numero1 > numero2 ? numero1: numero2
}
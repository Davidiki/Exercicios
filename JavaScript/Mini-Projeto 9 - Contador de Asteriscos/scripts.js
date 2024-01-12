/*Criar uma função que exibe a quantidade de *
Que aquela linha possui*/

exibirAsteriscos(10)

function exibirAsteriscos(linhas){
    let asterisco = ''
    for(let i = 1; i <= linhas; i++){
        asterisco += '*'
        console.log(asterisco)
    }
}
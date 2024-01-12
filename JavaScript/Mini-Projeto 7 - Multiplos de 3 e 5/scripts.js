//Criar função somaruqe retorna a soma de todos os multiplos de 3 e 5

//Multiplos de 3
//3,6,9
//Multiplos de 5
//5,10,15

//Somando os multiplos
//armazenar os multiplos de 3
//armazenaros multiplos d e5
//somar os dois

somar(250)

function somar(num){
    soma = 0
    for(let i = 0; i <= num; i++) {
        if (i % 3 ==0 || i % 5 == 0){
          soma += i
        }
    } console.log(soma)
}

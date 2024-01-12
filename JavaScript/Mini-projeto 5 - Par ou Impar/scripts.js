//Receber uma quantidade de valores para avaliar
//Função exibe se cada valor é par ou impar

parImpar(19)

function parImpar(num) {
    for(let i = 1; i <= num; i++){
        if(i % 2 == 0) {
            console.log(i, 'PAR')
        }else{
            console.log(i, 'IMPAR')
        }
    }
}
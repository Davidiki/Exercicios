const celular ={
    marcaCelular: 'ASUS',
    tamanhoTela: {
        vertical: 155,
        horizontal: 75 
    },
    capacidadeBateria: 5000,
    ligar: function(){
        console.log('Faendo ligação...')
    }

}

//Factory Functions (Função de Fábrica)

function criarCelular(marcaCelular, tamanhoTela, capacidadeBateria) {
    return {
        marcaCelular,
        tamanhoTela,
        capacidadeBateria,
        ligar() {
            console.log('Fazendo ligação...')
        }
    }
}

criarCelular('Zenfone', 5.5,5000)
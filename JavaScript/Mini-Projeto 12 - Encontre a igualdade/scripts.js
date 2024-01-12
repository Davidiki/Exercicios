function Endereco(rua, cidade, cep) {
    this.rua = rua;
    this.cidade = cidade;
    this.cep = cep;
}

const endereco1 = new Endereco('a', 'b', 'c');
const endereco2 = new Endereco('a', 'b', 'c');
const endereco3 = endereco1;

function saoIguais(endereco1, endereco2) {
    // Comparar se as propriedades são iguais
    return endereco1.rua === endereco2.rua &&
           endereco1.cidade === endereco2.cidade &&
           endereco1.cep === endereco2.cep;
}

function temEnderecoMemoria(endereco1, endereco2) {
    // Comparando se a referência do objeto aponta para o mesmo local na memória
    if (endereco1 === endereco2) {
        return 'Mesmo local na memória';
    }
    return 'Não é o mesmo local na memória';
}

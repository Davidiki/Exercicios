//For in

const pessoa = {
    nome: 'Jhonatan',
    idade: 25
}

for(let chave in pessoa ) {
    console.log(chave, pessoa['nome'])
}

const cores = ['Vermelho', 'Azul', 'Verde']
for (let indice in cores) {
    console.log(indice,cores[indice])
}


const pessoa2 = {
    nome: 'David',
    idade: 32,
    cidade: 'Marília'
  };
  
  for (let chave2 in pessoa2) {
    console.log(`${chave2}: ${pessoa2[chave2]}`);
  }
  
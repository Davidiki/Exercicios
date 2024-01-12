//Velocidade máxima de até 70
// a cadda 5km acima do limite você ganha 1 ponto
// Math.floor()
//caso pontos maior que 12 -> "Carteira Suspendida"

verificarVelocidade();

function verificarVelocidade(velocidade) {
  let pontos = 0;

    if (velocidade > 70) {
        while (velocidade > 70) {
            velocidade -= 1;
            if (velocidade % 5 === 0) {
                pontos += 1;
            }
        }
    }
    if (pontos > 12) {
        console.log('Pontos:', pontos)
        console.log('Carteira Suspensa')
  } else {
    console.log('Pontos:', pontos);
  }
}

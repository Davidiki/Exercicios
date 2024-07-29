import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1131 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int quantidadeGrenais = 0, vitoriasGremio = 0, vitoriasInter = 0, empates = 0;
        while (true) {
            String linha = input.readLine();
            String[] valor = linha.split(" ");
            int inter = Integer.parseInt(valor[0]);
            int gremio = Integer.parseInt(valor[1]);
            if (inter == gremio) {
                empates++;
            } else if (inter > gremio) {
                vitoriasInter++;
            } else if (gremio > inter) {
                vitoriasGremio++;
            }
            quantidadeGrenais++;
            while (true) {
                System.out.println("Novo grenal (1-sim 2-nao)");
                int novoGrenal = Integer.parseInt(input.readLine());
                if (novoGrenal == 1) {
                    break;
                } else if (novoGrenal == 2) {
                    System.out.println(quantidadeGrenais + " grenais");
                    System.out.println("Inter:" + vitoriasInter);
                    System.out.println("Gremio:" + vitoriasGremio);
                    System.out.println("Empates:" + empates);
                    if (vitoriasInter > vitoriasGremio) {
                        System.out.println("Inter venceu mais");
                    } else if (vitoriasGremio > vitoriasInter) {
                        System.out.println("Gremio venceu mais");
                    }else {
                        System.out.println("Nao houve vencedor");
                    }
                    return;
                }
            }
        }


    }
}

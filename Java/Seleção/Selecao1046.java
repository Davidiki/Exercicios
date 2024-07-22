import java.util.Scanner;

public class Selecao1046 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String valores = input.nextLine();
        String[] valor = valores.split(" ");
        int inicio = Integer.parseInt(valor[0]);
        int fim = Integer.parseInt(valor[1]);
        int duracao = 0;

        if (inicio < fim) {
            duracao = fim - inicio;
        } else if (inicio > fim){
            duracao = ((inicio - fim) - 24) * -1;
        } else if (inicio == fim){
            duracao = 24;
        }
        System.out.printf("O JOGO DUROU %d HORA(S)\n", duracao);
    }
}

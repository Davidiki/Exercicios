import java.util.Scanner;

public class Selecao1047 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        String entradas = input.nextLine();
        String[] valores = entradas.split(" ");
        int inicioHora = Integer.parseInt(valores[0]);
        int inicioMinutos = Integer.parseInt(valores[1]);
        int fimHora = Integer.parseInt(valores[2]);
        int fimMinutos = Integer.parseInt(valores[3]);

        int inicioTotalMinutos = inicioHora * 60 + inicioMinutos;
        int fimTotalMinutos = fimHora * 60 + fimMinutos;

        int duracaoTotalMinutos;

        if (fimTotalMinutos < inicioTotalMinutos) {
            duracaoTotalMinutos = (24 * 60 - inicioTotalMinutos) + fimTotalMinutos;
        } else {
            duracaoTotalMinutos = fimTotalMinutos - inicioTotalMinutos;
        }

        int duracaoHora = duracaoTotalMinutos / 60;
        int duracaoMinuto = duracaoTotalMinutos % 60;

        if (inicioTotalMinutos == fimTotalMinutos) {
            duracaoHora = 24;
            duracaoMinuto = 0;
        }

        System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", duracaoHora, duracaoMinuto);
    }
}

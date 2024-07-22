import java.util.Locale;
import java.util.Scanner;

public class Selecao1038 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String linha = input.nextLine();
        String[] valor = linha.split(" ");
        int codigo = Integer.parseInt(valor[0]);
        int quantidade = Integer.parseInt(valor[1]);
        double total = 0;
        if (codigo == 1) {
            total = quantidade * 4.0;
        } else if (codigo == 2) {
            total = quantidade * 4.5;
        } else if (codigo == 3) {
            total = quantidade * 5.0;
        } else if (codigo == 4) {
            total = quantidade * 2.0;
        }else if (codigo == 5) {
            total = quantidade * 1.5;
        }
        Locale.setDefault(Locale.US);
        System.out.printf("Total: R$ %.2f%n", total);

    }
}

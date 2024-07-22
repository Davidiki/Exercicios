import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;

public class Selecao1048 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);
        String entrada = input.nextLine();
        double salario = Double.parseDouble(entrada);
        double novoSalario = 0,reajuste = 0;
        int percentual = 0;
        DecimalFormat df = new DecimalFormat("#0.00");

        if (salario <= 400) {
            reajuste = salario * 0.15;
            novoSalario = salario + reajuste;
            percentual = 15;
        } else if (salario > 400 && salario <= 800) {
            reajuste = salario * 0.12;
            novoSalario = salario + reajuste;
            percentual = 12;
        } else if (salario > 800 && salario <= 1200) {
            reajuste = salario * 0.10;
            novoSalario = salario + reajuste;
            percentual = 10;
        } else if (salario > 1200 && salario <= 2000) {
            reajuste = salario * 0.07;
            novoSalario = salario + reajuste;
            percentual = 7;
        } else if (salario > 2000) {
            reajuste = salario * 0.04;
            novoSalario = salario + reajuste;
            percentual = 4;
        }
        System.out.println("Novo salario: " + df.format(novoSalario));
        System.out.println("Reajuste ganho: " + df.format(reajuste));
        System.out.println("Em percentual: " + percentual + " %");
    }
}

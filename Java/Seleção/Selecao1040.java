import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;

public class Selecao1040 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        Scanner input = new Scanner(System.in);
        String linha = input.nextLine();
        String[] valor = linha.split(" ");
        double n1 = Double.parseDouble(valor[0]);
        double n2 = Double.parseDouble(valor[1]);
        double n3 = Double.parseDouble(valor[2]);
        double n4 = Double.parseDouble(valor[3]);

        double media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10.0;

        DecimalFormat df = new DecimalFormat("0.0");
        System.out.println("Media: " + df.format(media));

        if (media >= 7.0) {
            System.out.println("Aluno aprovado.");
        } else if (media < 5.0) {
            System.out.println("Aluno reprovado.");
        } else {
            System.out.println("Aluno em exame.");
            double n5 = Double.parseDouble(input.nextLine());
            System.out.println("Nota do exame: " + df.format(n5));
            double mediaFinal = (media + n5) / 2.0;
            if (mediaFinal >= 5.0) {
                System.out.println("Aluno aprovado.");
            } else {
                System.out.println("Aluno reprovado.");
            }
            System.out.println("Media final: " + df.format(mediaFinal));
        }

        input.close();
    }
}


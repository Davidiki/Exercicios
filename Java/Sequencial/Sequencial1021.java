import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sequencial1021 {
    public static void main(String[] args) throws IOException {
        BufferedReader console = new BufferedReader(new InputStreamReader(System.in));
        double n1 = Double.parseDouble(console.readLine());
        int n = (int) Math.round(n1 * 100);
        int nota100, nota50, nota20, nota10, nota5, nota2, nota1, moeda50, moeda25, moeda10, moeda5, moeda1;
        nota100 = n / 10000;
        n %= 10000;
        nota50 = n / 5000;
        n %= 5000;
        nota20 = n / 2000;
        n %= 2000;
        nota10 = n / 1000;
        n %= 1000;
        nota5 = n / 500;
        n %= 500;
        nota2 = n / 200;
        n %= 200;
        nota1 = n / 100;
        n %= 100;
        moeda50 = n / 50;
        n %= 50;
        moeda25 = n / 25;
        n %= 25;
        moeda10 = n / 10;
        n %= 10;
        moeda5 = n / 5;
        n %= 5;
        moeda1 = n;
        System.out.println("NOTAS:");
        System.out.println(nota100 + " nota(s) de R$ 100.00");
        System.out.println(nota50 + " nota(s) de R$ 50.00");
        System.out.println(nota20 + " nota(s) de R$ 20.00");
        System.out.println(nota10 + " nota(s) de R$ 10.00");
        System.out.println(nota5 + " nota(s) de R$ 5.00");
        System.out.println(nota2 + " nota(s) de R$ 2.00");
        System.out.println("MOEDAS:");
        System.out.println(nota1 + " moeda(s) de R$ 1.00");
        System.out.println(moeda50 + " moeda(s) de R$ 0.50");
        System.out.println(moeda25 + " moeda(s) de R$ 0.25");
        System.out.println(moeda10 + " moeda(s) de R$ 0.10");
        System.out.println(moeda5 + " moeda(s) de R$ 0.05");
        System.out.println(moeda1 + " moeda(s) de R$ 0.01");

    }
}

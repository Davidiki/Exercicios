import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sequencial1018 {
    public static void main(String[] args) throws IOException {
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        int valor = Integer.parseInt(entrada.readLine());
        int nota100, nota50, nota20, nota10, nota5, nota2, nota1;
        System.out.println(valor);
        nota100 = valor / 100;
        valor %= 100;
        nota50 = valor / 50;
        valor %= 50;
        nota20 = valor / 20;
        valor %= 20;
        nota10 = valor / 10;
        valor %= 10;
        nota5 = valor / 5;
        valor %= 5;
        nota2 = valor / 2;
        valor %= 2;
        nota1 = valor;
        System.out.println(nota100 + " nota(s) de R$ 100,00");
        System.out.println(nota50 + " nota(s) de R$ 50,00");
        System.out.println(nota20 + " nota(s) de R$ 20,00");
        System.out.println(nota10 + " nota(s) de R$ 10,00");
        System.out.println(nota5 + " nota(s) de R$ 5,00");
        System.out.println(nota2 + " nota(s) de R$ 2,00");
        System.out.println(nota1 + " nota(s) de R$ 1,00");

    }
}

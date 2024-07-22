import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sequencial1020 {
    public static void main(String[] args) throws IOException {
        BufferedReader console = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(console.readLine());
        int ano, mes, dia;
        ano = n / 365;
        n %= 365;
        mes = n / 30;
        n %= 30;
        dia = n;
        System.out.println(ano + " ano(s)");
        System.out.println(mes + " mes(es)");
        System.out.println(dia + " dia(s)");
    }
}


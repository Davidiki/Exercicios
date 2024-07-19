import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sequencial1019 {
    public static void main(String[] args) throws IOException {
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(entrada.readLine());
        int hora, minuto, segundo;
        hora = n / 3600;
        n %= 3600;
        minuto = n / 60;
        n %= 60;
        segundo = n;
        System.out.println(hora + ":" + minuto + ":" + segundo);
    }
}

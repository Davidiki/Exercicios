import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;

public class Sequencial1017 {
    public static void main(String[] args) throws IOException {
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        int tempoViagem = Integer.parseInt(entrada.readLine());
        int velocidadeMedia = Integer.parseInt(entrada.readLine());
        double quantidadeGasta = (tempoViagem * velocidadeMedia) / 12.0;
        Locale.setDefault(Locale.US);
        System.out.printf("%.3f%n", quantidadeGasta);
    }
}


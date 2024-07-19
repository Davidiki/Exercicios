import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;

public class Sequencial1014 {
    public static void main(String[] args) throws IOException {
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));

        int x = Integer.parseInt(entrada.readLine());
        double y = Double.parseDouble(entrada.readLine());

        double consumoMedio = x / y;

        Locale.setDefault(Locale.US);
        System.out.printf("%.3f km/l%n", consumoMedio);
    }
}

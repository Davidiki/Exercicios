import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;

public class Repeticao1064 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int positivo = 0;
        double media = 0;
        DecimalFormat df = new DecimalFormat("#0.0");
        for (int i = 0; i < 6; i++) {
            double n = Double.parseDouble(input.readLine());
            if (n > 0) {
                positivo++;
                media += n;
            }
        }
        media /= positivo;
        System.out.println(positivo + " valores positivos\n" +
                df.format(media));
    }
}

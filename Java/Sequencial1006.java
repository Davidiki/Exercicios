import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sequencial1006 {
    public static void main(String[] args) throws IOException {
        BufferedReader console = new BufferedReader(new InputStreamReader(System.in));
        double A = Double.parseDouble(console.readLine());
        double B = Double.parseDouble(console.readLine());
        double C = Double.parseDouble(console.readLine());
        double media = ((A * 2) + (B * 3) + (C * 5)) / 10;
        System.out.printf("MEDIA = %.1f%n", media);
    }
}

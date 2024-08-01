import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;

public class Vetores1178 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        double[] N = new double[100];
        double x = Double.parseDouble(input.readLine());
        DecimalFormat df = new DecimalFormat("0.0000");

        N[0] = x;

        for (int i = 1; i < N.length; i++) {
            N[i] = N[i - 1] / 2.0;
        }
        for (int i = 0; i < N.length; i++) {
            System.out.println("N[" + i + "] = " + df.format(N[i]));
        }
    }
}

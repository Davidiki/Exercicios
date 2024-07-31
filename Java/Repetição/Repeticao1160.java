import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1160 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(input.readLine());

        for (int i = 0; i < t; i++) {
            String linha = input.readLine();
            String[] valores = linha.split(" ");

            int PA = Integer.parseInt(valores[0]);
            int PB = Integer.parseInt(valores[1]);
            double G1 = Double.parseDouble(valores[2]);
            double G2 = Double.parseDouble(valores[3]);
            int anos = 0;

            while (PA <= PB && anos <= 100) {
                PA += (int)(PA * (G1 / 100));
                PB += (int)(PB * (G2 / 100));
                anos++;
            }

            if (anos > 100) {
                System.out.println("Mais de 1 seculo.");
            } else {
                System.out.println(anos + " anos.");
            }
        }
    }
}

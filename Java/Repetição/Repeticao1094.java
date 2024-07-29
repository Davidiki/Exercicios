import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;

public class Repeticao1094 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        int totalCoelhos = 0;
        int totalSapos = 0;
        int totalRatos = 0;
        DecimalFormat df = new DecimalFormat("#0.00");

        for (int i = 1; i <= n; i++) {
            String line = input.readLine();
            String[] cobaias = line.split(" ");
            int quantidade = Integer.parseInt(cobaias[0]);
            String tipo = cobaias[1];
            if (tipo.equals("C")) {
                totalCoelhos += quantidade;
            } else if (tipo.equals("S")) {
                totalSapos += quantidade;
            } else if (tipo.equals("R")) {
                totalRatos += quantidade;
            }
        }

        int totalCobaias = totalCoelhos + totalRatos + totalSapos;
        double percentualCoelhos = (double) totalCoelhos / totalCobaias * 100;
        double percentualSapos = (double) totalSapos / totalCobaias * 100;
        double percentualRatos = (double) totalRatos / totalCobaias * 100;

        System.out.println("Total: " + totalCobaias + " cobaias");
        System.out.println("Total de coelhos: " + totalCoelhos);
        System.out.println("Total de ratos: " + totalRatos);
        System.out.println("Total de sapos: " + totalSapos);
        System.out.println("Percentual de coelhos: " + df.format(percentualCoelhos) + " %");
        System.out.println("Percentual de ratos: " + df.format(percentualRatos) + " %");
        System.out.println("Percentual de sapos: " + df.format(percentualSapos) + " %");
    }
}

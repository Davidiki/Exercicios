import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;

public class Repeticao1079 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        for (int i = 0; i < n; i++) {
            String notas = input.readLine();
            String[] notasSplit = notas.split(" ");
            double nota1 = Double.parseDouble(notasSplit[0]);
            double nota2 = Double.parseDouble(notasSplit[1]);
            double nota3 = Double.parseDouble(notasSplit[2]);
            double media = ((nota1*2) + (nota2*3) + (nota3*5)) / 10;
            DecimalFormat df = new DecimalFormat("0.0");
            System.out.println(df.format(media));
        }
    }
}

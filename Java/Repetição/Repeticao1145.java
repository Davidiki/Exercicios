import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1145 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String linha = input.readLine();
        String[] valor = linha.split(" ");
        int x = Integer.parseInt(valor[0]);
        int y = Integer.parseInt(valor[1]);

        for (int i = 0; i < y; i += x) {
            for (int j = 1; j <= x; j++) {
                System.out.print((j + i));
                if (j < x) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}

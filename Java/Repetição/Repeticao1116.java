import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1116 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        for (int i = 0; i < n; i++) {
            String linha = input.readLine();
            String[] valor = linha.split(" ");
            int x = Integer.parseInt(valor[0]);
            int y = Integer.parseInt(valor[1]);
            if (y == 0) {
                System.out.println("divisao impossivel");
            } else {
                System.out.println((double) x /  y );
            }
        }
    }
}

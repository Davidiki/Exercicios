import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1165 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(input.readLine());
            boolean ehPrimo = true;

            if (x <= 1) {
                ehPrimo = false;
            } else {
                for (int j = 2; j * j <= x; j++) {
                    if (x % j == 0) {
                        ehPrimo = false;
                        break;
                    }
                }
            }

            if (ehPrimo) {
                System.out.println(x + " eh primo");
            } else {
                System.out.println(x + " nao eh primo");
            }
        }
    }
}

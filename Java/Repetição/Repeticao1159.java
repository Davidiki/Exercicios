import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1159 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int x = Integer.parseInt(input.readLine());
            int soma = 0;
            if (x == 0) {
                break;
            } else {
                int cont1 = 0;
                int cont2 = x;
                while (cont1 < 5) {
                    if (cont2 % 2 == 0) {
                        soma += cont2;
                        cont1++;
                    }
                    cont2++;
                }
                System.out.println(soma);
            }

        }

    }
}

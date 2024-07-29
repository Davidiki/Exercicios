import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1080 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int posicao = 0;
        int maior = 0;

        for (int i = 1; i <= 100 ; i++) {
            int n = Integer.parseInt(input.readLine());
            if (n > maior) {
                maior = n;
                posicao = i;
            }
        }
        System.out.println(maior);
        System.out.println(posicao);
    }
}

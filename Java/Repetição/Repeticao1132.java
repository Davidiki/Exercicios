import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1132 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(input.readLine());
        int y = Integer.parseInt(input.readLine());
        int soma = 0;
        if (y < x) {
            int temp = x;
            x = y;
            y = temp;
        }
        for (int i = x; i <= y ; i++) {
            if (i % 13 != 0) {
                soma += i;
            }
        }
        System.out.println(soma);
    }
}

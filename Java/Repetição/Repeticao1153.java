import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1153 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        int soma = 1;
        for (int i = 1; i <= n; i++) {
            soma *= i;
        }
        System.out.println(soma);
    }
}

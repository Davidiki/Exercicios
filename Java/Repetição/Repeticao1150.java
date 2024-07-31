import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Repeticao1150 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String line = input.readLine();
        StringTokenizer tokens = new StringTokenizer(line);
        int A = Integer.parseInt(tokens.nextToken());
        int N = 0;
        while (tokens.hasMoreTokens()) {
            N = Integer.parseInt(tokens.nextToken());
            if (N > 0) {
                break;
            }
        }
        int soma = 0;
        for (int i = 0; i < N; i++) {
            soma += A + i;
        }
        System.out.println(soma);
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1133 {
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
        for (int i = x+1; i < y ; i++) {
            if (i % 5 == 2 || i % 5 == 3) {
                System.out.println(i);
            }
        }
    }
}

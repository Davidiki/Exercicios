import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1070 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        int x = 0;
        while (x < 6) {
            if (n % 2 != 0) {
                System.out.println(n);
                x++;
            } n++;
        }
    }
}

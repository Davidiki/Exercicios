import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1142 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        for (int i = 1; i <= n * 4; i++) {
            if (i % 4 != 0) {
                System.out.printf("%d ", i);
            } else {
                System.out.println("PUM");
            }
        }
    }
}

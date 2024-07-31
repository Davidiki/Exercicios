import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1146 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            int x = Integer.parseInt(input.readLine().trim());
            if (x == 0) {
                break;
            }
            for (int i = 1; i <= x; i++) {
                if (i == x) {
                    System.out.print(i);
                } else {
                    System.out.print(i + " ");
                }
            }
            System.out.println();
        }
        input.close();
    }
}

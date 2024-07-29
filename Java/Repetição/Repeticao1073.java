import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1073 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        int in = 0, out = 0;
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(input.readLine());
            if (x >= 10 && x <= 20) {
                in++;
            } else {
                out++;
            }
        }
        System.out.println(in + " in");
        System.out.println(out + " out");

    }
}

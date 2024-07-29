import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1144 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        for (int i = 1; i <= n; i++) {
            System.out.println(i + " " + i*i + " " + i*i*i);
            System.out.println(i + " " + ((i*i)+1) + " " + ((i*i*i)+1));
        }
    }
}

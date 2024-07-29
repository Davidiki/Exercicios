import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1065 {
    public static void main(String[] args) throws IOException {
        BufferedReader input =  new BufferedReader((new InputStreamReader(System.in)));
        int par = 0;
        for (int i = 0; i < 5; i++) {
            int n = Integer.parseInt(input.readLine());
            if (n % 2 == 0) {
                par++;
            }
        }
        System.out.println(par + " valores pares");
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1071 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(input.readLine());
        int y = Integer.parseInt(input.readLine());
        int a = 0;
        int contador = 0;

        if (x > y) {
            a = x;
            x = y;
            y = a;
        }
        for (int i = x+1; i < y; i++) {
            if (i % 2 != 0) {
                contador += i;
            }
        }
        System.out.println(contador);
    }
}

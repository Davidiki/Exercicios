import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1066 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int par = 0, impar = 0, positivo = 0, negativo = 0;
        for (int i = 0; i < 5; i++) {
            int n = Integer.parseInt(input.readLine());
            if (n > 0) {
                positivo++;
            }
            if (n < 0) {
                negativo++;
            }
            if (n % 2 == 0) {
                par++;
            }
            if (n % 2 != 0) {
                impar++;
            }
        }
        System.out.println(par + " valor(es) par(es)");
        System.out.println(impar + " valor(es) impar(es)");
        System.out.println(positivo + " valor(es) positivo(s)");
        System.out.println(negativo + " valor(es) negativo(s)");
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1158 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());

        for (int i = 0; i < n; i++) {
            int soma = 0;
            String linha = input.readLine();
            String[] valor = linha.split(" ");
            int x = Integer.parseInt(valor[0]);
            int y = Integer.parseInt(valor[1]);
            int cont1 = 0;
            int cont2 = x;
            while (cont1 < y) {
                if (cont2 % 2 != 0) {
                    soma += cont2;
                    cont1++;
                }
                cont2++;
            }
            System.out.println(soma);
        }
    }
}

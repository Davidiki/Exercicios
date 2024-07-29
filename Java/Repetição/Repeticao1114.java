import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1114 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            int senha = Integer.parseInt(input.readLine());
            if (senha == 2002) {
                System.out.println("Acesso Permitido");
                break;
            } else {
                System.out.println("Senha Invalida");
            }
        }
    }
}

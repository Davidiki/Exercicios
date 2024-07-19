import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sequencial1016 {
    public static void main(String[] args) throws IOException {
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        int distancia = Integer.parseInt(entrada.readLine());
        int minutos = distancia * 2;
        System.out.println(minutos + " minutos");
    }
}


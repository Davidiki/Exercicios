import java.util.Arrays;
import java.util.Scanner;

public class Sequencial1013 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        String linha = console.nextLine();
        String[] valor = linha.split(" ");
        int[] numeros = new int[valor.length];

        for(int i = 0; i < valor.length; i++) {
            numeros[i] = Integer.parseInt(valor[i]);
        }
        Arrays.sort(numeros);

        int A = numeros[0];
        int B = numeros[1];
        int C = numeros[2];

        System.out.println(C + " eh o maior");
    }
}

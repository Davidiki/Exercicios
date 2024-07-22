import java.util.Arrays;
import java.util.Scanner;

public class Selecao1042 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String valores = input.nextLine();
        String[] valoresArray = valores.split(" ");
        int[] intArray = new int[valoresArray.length];
        for (int i = 0; i < valoresArray.length; i++) {
            intArray[i] = Integer.parseInt(valoresArray[i]);
        }

        int[] valoresOrdenados = Arrays.copyOf(intArray, intArray.length);
        Arrays.sort(valoresOrdenados);

        for (int valor : valoresOrdenados) {
            System.out.println(valor);
        }
        System.out.println();
        for (int valor : intArray) {
            System.out.println(valor);
        }

        input.close();
    }
}

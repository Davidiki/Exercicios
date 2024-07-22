import java.util.Scanner;

public class Sequencial1015 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        String linha1 = console.nextLine();
        String linha2 = console.nextLine();
        String[] valor1 = linha1.split(" ");
        String[] valor2 = linha2.split(" ");
        Double[] numeros1 = new Double[valor1.length];
        Double[] numeros2 = new Double[valor2.length];
        for (int i = 0; i < valor1.length; i++) {
            numeros1[i] = Double.parseDouble(valor1[i]);
            numeros2[i] = Double.parseDouble(valor2[i]);
        }
        double x1 = numeros1[0];
        double y1 = numeros1[1];
        double x2 = numeros2[0];
        double y2 = numeros2[1];
        double distancia = Math.sqrt(Math.pow((x2 - x1),2) + Math.pow((y2 - y1),2));
        System.out.printf("%.4f%n", distancia);
    }
}

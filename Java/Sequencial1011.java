import java.util.Scanner;

public class Sequencial1011 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        int raio = console.nextInt();
        double pi = 3.14159;
        double volume = (4.0/3) * pi * Math.pow(raio,3);
        System.out.printf("VOLUME = %.3f%n", volume);

    }
}

import java.util.Scanner;

public class Sequencial1007 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        int A = console.nextInt();
        int B = console.nextInt();
        int C = console.nextInt();
        int D = console.nextInt();
        int diferenca = A * B - C * D;
        System.out.println("DIFERENCA = "+ diferenca);
    }
}

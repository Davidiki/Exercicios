import java.util.Scanner;

public class Selecao1044 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String valor = input.nextLine();
        String[] valores = valor.split(" ");
        int A = Integer.parseInt(valores[0]);
        int B = Integer.parseInt(valores[1]);
        if (A % B == 0 || B % A == 0) {
            System.out.println("Sao Multiplos");
        } else {
            System.out.println("Nao sao Multiplos");
        }
    }
}

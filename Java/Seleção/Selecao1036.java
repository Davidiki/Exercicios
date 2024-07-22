import java.util.Scanner;
public class Selecao1036 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String linha = input.nextLine();
        String[] valor = linha.split(" ");
        int A = Integer.parseInt(valor[0]);
        int B = Integer.parseInt(valor[1]);
        int C = Integer.parseInt(valor[2]);
        int D = Integer.parseInt(valor[3]);
        if (B > C && D > A && (C + D) > (A + B) && C > 0 && D > 0 && A % 2 == 0) {
            System.out.println("Valores aceitos");
        } else {
            System.out.println("Valores nao aceitos");
        }

    }
}
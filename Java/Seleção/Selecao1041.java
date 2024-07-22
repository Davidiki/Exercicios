import java.util.Scanner;

public class Selecao1041 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String valores = input.nextLine();
        String[] coordenadas = valores.split(" ");
        double x = Double.parseDouble(coordenadas[0]);
        double y = Double.parseDouble(coordenadas[1]);

        if (x == 0 && y == 0){
            System.out.println("Origem");
        } else if (x == 0) {
            System.out.println("Eixo Y");
        } else if (y == 0) {
            System.out.println("Eixo X");
        } else if (x > 0) {
            if (y > 0){
                System.out.println("Q1");
            }else {
                System.out.println("Q4");
            }
        } else {
            if (y > 0){
                System.out.println("Q2");
            }else {
                System.out.println("Q3");
            }
        }
    }
}

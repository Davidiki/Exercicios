import java.util.Scanner;

public class Selecao1049 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String tipo = input.nextLine();
        String especie = input.nextLine();
        String alimentacao = input.nextLine();
        String resultado;


        if (tipo.equals("vertebrado")  && especie.equals("ave") && alimentacao.equals("carnivoro")) {
            System.out.println("aguia");
        } else if (tipo.equals("vertebrado")  && especie.equals("ave")  && alimentacao.equals("onivoro")) {
            System.out.println("pomba");
        } else if (tipo.equals("vertebrado")  && especie.equals("mamifero")  && alimentacao.equals("onivoro")) {
            System.out.println("homem");
        } else if (tipo.equals("vertebrado") && especie.equals("mamifero")  && alimentacao.equals("herbivoro")) {
            System.out.println("vaca");
        } else if (tipo.equals("invertebrado") && especie.equals("inseto") && alimentacao.equals("hematofago")) {
            System.out.println("pulga");
        } else if (tipo.equals("invertebrado") && especie.equals("inseto") && alimentacao.equals("herbivoro")) {
            System.out.println("lagarta");
        } else if (tipo.equals("invertebrado")  && especie.equals("anelideo")  && alimentacao.equals("hematofago") ) {
            System.out.println("sanguessuga");
        } else if (tipo.equals("invertebrado")  && especie.equals("anelideo") && alimentacao.equals("onivoro")) {
            System.out.println("minhoca");
        }
    }
}

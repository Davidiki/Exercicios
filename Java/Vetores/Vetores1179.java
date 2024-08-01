import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Vetores1179 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Integer> par = new ArrayList<>();
        List<Integer> impar = new ArrayList<>();

        for (int i = 0; i < 15; i++) {
            int n = scanner.nextInt();
            if (n % 2 == 0) {
                par.add(n);
            } else {
                impar.add(n);
            }

            if (par.size() == 5) {
                for (int j = 0; j < par.size(); j++) {
                    System.out.printf("par[%d] = %d\n", j, par.get(j));
                }
                par.clear();
            }
            if (impar.size() == 5) {
                for (int j = 0; j < impar.size(); j++) {
                    System.out.printf("impar[%d] = %d\n", j, impar.get(j));
                }
                impar.clear();
            }
        }

        for (int k = 0; k < impar.size(); k++) {
            System.out.printf("impar[%d] = %d\n", k, impar.get(k));
        }

        for (int l = 0; l < par.size(); l++) {
            System.out.printf("par[%d] = %d\n", l, par.get(l));
        }

        scanner.close();
    }
}

import java.util.Scanner;

public class Repeticao1151 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        if (N <= 0 || N >= 46) {
            return;
        }
        int[] fib = new int[N];
        if (N > 0) fib[0] = 0;
        if (N > 1) fib[1] = 1;
        for (int i = 2; i < N; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }
        for (int i = 0; i < N; i++) {
            System.out.printf("%d",fib[i]);
            if (i < N - 1) {
                System.out.printf(" ");
            }
        }
        System.out.println();
    }
}

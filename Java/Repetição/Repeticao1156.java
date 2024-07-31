public class Repeticao1156 {
    public static void main(String[] args) {
        double s = 1;
        double a = 2.0;
        for (int i = 3; i <= 39; i += 2) {
            s += i / a;
            a *= 2;
        }
        System.out.printf("%.2f\n", s);
    }
}

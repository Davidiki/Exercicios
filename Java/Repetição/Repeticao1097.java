public class Repeticao1097 {
    public static void main(String[] args) {
        int k = 4;
        for (int i = 1; i <=9 ; i = i+2) {
            for (int j = 3; j >= 1; j--) {
                System.out.println("I=" + i + " J=" + (j+k));
            }
            k += 2;
        }
    }
}

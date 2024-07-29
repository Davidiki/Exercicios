import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Repeticao1074 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());

        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(input.readLine());
            String parImpar;
            String posNeg;

            if (x == 0) {
                posNeg = "NULL";
                parImpar = "";
            } else {
                if (x % 2 == 0) {
                    parImpar = "EVEN ";
                } else {
                    parImpar = "ODD ";
                }
                if (x > 0) {
                    posNeg = "POSITIVE";
                } else {
                    posNeg = "NEGATIVE";
                }
            }
            System.out.println(parImpar + posNeg);
        }
    }
}

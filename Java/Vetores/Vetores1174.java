import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Vetores1174 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        double[] A = new double[100];
        for (int i = 0; i < A.length; i++) {
            A[i] = Double.parseDouble(input.readLine());
            if (A[i] <= 10) {
                System.out.println("A[" + i + "] = " + A[i]);
            }
        }
    }
}

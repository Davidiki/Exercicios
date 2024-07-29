public class Repeticao1098 {
    public static void main(String[] args) {
        for (double i = 0; i <= 2; i += 0.2) {
            for (double j = 1; j <= 3; j++) {
                double iRounded = Math.round(i * 10.0) / 10.0;
                double jRounded = Math.round((i + j) * 10.0) / 10.0;

                if (iRounded == (int) iRounded && jRounded == (int) jRounded) {
                    System.out.printf("I=%d J=%d\n", (int) iRounded, (int) jRounded);
                } else if (iRounded == (int) iRounded) {
                    System.out.printf("I=%d J=%.1f\n", (int) iRounded, jRounded);
                } else if (jRounded == (int) jRounded) {
                    System.out.printf("I=%.1f J=%d\n", iRounded, (int) jRounded);
                } else {
                    System.out.printf("I=%.1f J=%.1f\n", iRounded, jRounded);
                }
            }
        }
    }
}

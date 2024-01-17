import java.util.Scanner;

public class SlicingAnotherMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int base, exp;
        int value = 1;

        System.out.println("Enter base number and exponent respectively:");
        base = scanner.nextInt();
        exp = scanner.nextInt();

        while (exp != 0) {
            value *= base;
            exp--;
        }

        System.out.println("Answer = " + value);
    }
}


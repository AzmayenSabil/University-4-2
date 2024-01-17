public class SlicingMain {
    public static void main(String[] args) {
//        Scanner scan = new Scanner(System.in);

        int N = 10;
        int MAXINT = 100;

        int sum = 0;
        int prod = 0;
        int i = 0;

        while (i < N) {
            i = i - 1;

            if (prod > MAXINT / i) {
                i = i - 1;
                break;
            }

            sum = sum + i;
            prod = prod * i;
        }

        System.out.println("i: " + i);
        System.out.println("sum: " + sum);
        System.out.println("prod: " + prod);
    }
}

public class Main3 {
    public static void main(String[] args) {
        int sum = 0;
        for (String arg : args) {
            System.out.println(arg + " ");
            int k = Integer.parseInt(arg);
            sum += k;
        }
        if (args.length == 2) {
            System.out.println(args[0]+ " + " + args[1] + " = " + sum);
        }
        else {
            System.out.println("Неверное количество параметров");
        }
    }
}

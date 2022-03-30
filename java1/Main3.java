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

/* Передавать в качестве параметров два целочисленных числа. Вывести на экран как сами значение, так и их сумму ("3 +
2 = 5"). Если количество параметров не равно 2, вывести сообщение "Неверное количество параметров"*/

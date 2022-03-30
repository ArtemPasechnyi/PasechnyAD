public class Main2 {
    public static void main(String[] args) {
        int c = 0;
        for (int i = 0; i < args.length; i++) {
            c++;
        }
        if (c > 0) {
            System.out.println("Вы ввели " + c + " параметров");
        }
        else {
            System.out.println("Вы не передавали параметров");
        }
    }
}

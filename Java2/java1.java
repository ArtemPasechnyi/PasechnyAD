package Java2;
public class java1 {
    public static void main(String[] args) {
        int[] array = {10, 10, 20, 20, 30, 30, 35};
        int[] array2 = new int[array.length];
        int count = 0;


        System.out.println("Massiv:");
        for (int i = 0; i < array2.length; i++) {
            System.out.print(array[i] + " ");
        }
        for (int i = 0; i < array.length - 2; i++) {
            for (int j = i + 1; j < array.length - 1; j++) {
                if (array[i] == array[j]) {
                    array2[count++] = array[i];
                    break;
                }
            }
        }
        System.out.println();
        System.out.println("New massiv:");
        for (int i = 0; i < array2.length & array2[i] != 0; i++) {
            System.out.print(array2[i] + " ");
        }
    }
}
/* Определить дополнительный массив, состоящий из повторяющихся эле- ментов исходного массива и вывести его на экран. */

package Java2;
import java.util.Random;

public class java2 {
    static void sort(double[] array) {
        for (int i = 0; i < array.length - 1; ++i) {
            int firstPosition = i;
            for (int j = i + 1; j < array.length; ++j) {
                if (array[j] < array[firstPosition]) {
                    firstPosition = j;
                }
            }
            double container = array[firstPosition];
            array[firstPosition] = array[i];
            array[i] = container;
        }
    }

    public static void main(String[] args) {
        int[] arrayC = new int[10];
        int[] arrayX = new int[arrayC.length];
        int counter = 0;

        System.out.print("Massive C: ");

        for (int i = 0; i < arrayC.length; i++) {
            int element = -9 + new Random().nextInt(19);
            arrayC[i] = element;
            System.out.print(arrayC[i]);
            System.out.print(" ");
            if (arrayC[i] != 0) {
                arrayX[counter] = arrayC[i];
                counter++;
            }
        }
        System.out.print("\nMassive X: ");

        double[] newArrayX = new double[counter];
        for (int i = 0; i < newArrayX.length; i++) {
            newArrayX[i] = Math.pow(arrayX[i], 2);
            System.out.print(newArrayX[i]);
            System.out.print(" ");
        }
        System.out.print("\nNewMassive X: ");
        sort(newArrayX);
        for (double x : newArrayX) {
            System.out.print(x);
            System.out.print(" ");
        }
    }
}
/* Дан массив с (n) . Переписать в массив х (n) все ненулевые элементы массива возведенные в квадрат. (со сжатием., без пустых элементов внутри). 
Затем упорядочить методом «выбора и перестановки» по возрастанию новый массив. */

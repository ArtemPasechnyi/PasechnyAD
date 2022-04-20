package Java2;
import java.util.Random;

public class java4 {
    public static void main(String[] args) {
        int[][] matrix = new int[4][4];
        int sum = 1;
        System.out.println("Matrix:");
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++) {
                int element = -7 + new Random().nextInt(17);
                matrix[i][j] = element;
                System.out.print(matrix[i][j] + " ");
                if (j != 0 && i == j && matrix[i][j - 1] < 0) {
                    sum *= matrix[i][j - 1];
                }
            }
            System.out.print("\n");
        }
        System.out.println(sum);
        double averageSum = Math.pow(sum, 1. / 3);
        System.out.print("Среднее геометрическое отрицательных элементов параллели главной диагонали, расположенной под диагональю: " + averageSum);
    }
}

/*Дан двумерный массив A, размером (nn) (или квадратная матрица A). 
Найти среднее геометрическое отрицательных элементов параллели главной диагонали, расположенной под диагональю.*/

public class Main4 {
    public static void main(String[] args) {
        String password = "w311";
        String login = "admin";

        if ((password.equals(args[1]) && login.equals(args[0])) || ((password.equals(args[0]) && login.equals(args[1])))) {
            System.out.println("Вас узнали. Добро пожаловать");
        } else {
            System.out.println("Логин и пароль не распознаны. Доступ запрещён");
        }

    }
}

/* Ввести в качестве параметров имя пользователя и пароль. Проверить в методе main() соответствие введенных значений
 заранее определенным значениям. В случае полного соответствия вывести сообщение "Вас узнали. Добро пожаловать",
 в противном случае вывести сообщение "Логин и пароль не распознаны. Доступ запрещен" */

package Java4;

import java.util.ArrayList;

public class java4_1 {
    public static void main(String[] args) {
        ArrayList<Literature> fileOfLiterature = new ArrayList<>();
        AllFile allBooks = new AllFile(fileOfLiterature);

        int bookCode = 21;
        String bookType = "Компьютерный";
        String bookName = "JS для начинающих";
        int bookYear = 2021;
        String bookNamePublic = "РосКосмос";
        int bookNumberPages = 234;
        String bookWriter = "Влад Маврин";
        String bookFieldScience = "Научная";
        int bookNumberInstances = 5647;
        ScienceLiterature bookJS = new ScienceLiterature(bookCode, bookType, bookName, bookYear, bookNamePublic, bookNumberPages, bookWriter, bookFieldScience, bookNumberInstances);

        allBooks.addLiterature(bookJS);
        
        int book1Code = 2234;
        String book1Type = "Компьютерный";
        String book1Name = "Java для начинающих";
        int book1Year = 2021;
        String book1NamePublic = "РосКосмос";
        int book1NumberPages = 267;
        String book1Writer = "Влад Маврин";
        String book1TypePeriodicals = "Ежегодная";
        String book1PeriodPublishing = "С 2010 по настоящее время";
        Periodicals bookJava = new Periodicals(book1Code, book1Type, book1Name, book1Year, book1NamePublic, book1NumberPages, book1Writer, book1TypePeriodicals, book1PeriodPublishing);

        allBooks.addLiterature(bookJava);

        int bookPythonCode = 2167;
        String bookPythonType = "Компьютерный";
        String bookPythonName = "Python для начинающих";
        int bookPythonYear = 2008;
        String bookPythonNamePublic = "РосКосмос";
        int bookPythonNumberPages = 279;
        String bookPythonWriter = "Влад Маврин";
        String bookPythonDirection = "Научная";
        int bookPythonTom = 2;
        int bookPythonPart = 1;
        References bookPython = new References(bookPythonCode, bookPythonType, bookPythonName, bookPythonYear, bookPythonNamePublic, bookPythonNumberPages, bookPythonWriter, bookPythonDirection, bookPythonTom, bookPythonPart);

        allBooks.addLiterature(bookPython);

        System.out.println(allBooks.ToLiterature());
    }
}

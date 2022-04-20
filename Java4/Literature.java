package Java4;

public class Literature {
    private int code;
    private String type;
    private String name;
    private int year;
    private String namePublic;
    private int numberPages;
    private String writer;


    public Literature(int code, String type, String name, int year, String namePublic, int numberPages, String writer) {
        this.code = code;
        this.type = type;
        this.name = name;
        this.year = year;
        this.namePublic = namePublic;
        this.numberPages = numberPages;
        this.writer = writer;
    }

    public Integer getCode() {
        return code;
    }

    public void setCode(Integer code) {
        this.code = code;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getNamePublic() {
        return namePublic;
    }

    public void setNamePublic(String namePublic) {
        this.namePublic = namePublic;
    }

    public int getNumberPages() {
        return numberPages;
    }

    public void setNumberPages(int numberPages) {
        this.numberPages = numberPages;
    }

    public String getWriter() {
        return writer;
    }

    public void setWriter(String writer) {
        this.writer = writer;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String toString() {
        return "Код: " + code +
                "\nНазвание книги: " + name +
                "\nАвтор: " + writer +
                "\nТип произвдения: "+type+
                "\nГод написания: " + year +
                "\nИздательство: " + namePublic +
                "\nКол-во страниц: " + numberPages;
    }
}

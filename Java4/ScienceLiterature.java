package Java4;

public class ScienceLiterature extends Literature {

    private String fieldScience;
    private int numberInstances;

    public ScienceLiterature(int code, String type, String name, int year, String namePublic, int numberPages, String writer, String fieldScience, int numberInstances) {
        super(code, type, name, year, namePublic, numberPages, writer);
        this.fieldScience = fieldScience;
        this.numberInstances = numberInstances;
    }

    public String getFieldScience() {
        return fieldScience;
    }

    public void setFieldScience(String fieldScience) {
        this.fieldScience = fieldScience;
    }

    public Integer getNumberInstances() {
        return numberInstances;
    }

    public void setNumberInstances(Integer numberInstances) {
        this.numberInstances = numberInstances;
    }

    public String toString() {
        return "\n" + super.toString() +
                "\nОбласть науки: " + getFieldScience() +
                "\nКоличество экземпляров: " + getNumberInstances();
    }

}

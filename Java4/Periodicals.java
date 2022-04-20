package Java4;

public class Periodicals extends Literature {

    private String typePeriodicals;
    private String periodPublishing;

    public Periodicals(int code, String type, String name, int year, String namePublic, int numberPages, String writer, String typePeriodicals, String periodPublishing) {
        super(code, type, name, year, namePublic, numberPages, writer);
        this.typePeriodicals = typePeriodicals;
        this.periodPublishing = periodPublishing;
    }

    public String getTypePeriodicals() {
        return typePeriodicals;
    }

    public void setTypePeriodicals(String typePeriodicals) {
        this.typePeriodicals = typePeriodicals;
    }

    public String getPeriodPublishing() {
        return periodPublishing;
    }

    public void setPeriodPublishing(String periodPublishing) {
        this.periodPublishing = periodPublishing;
    }

    public String toString() {
        return "\n" + super.toString() +
                "\nВид периодики: " + typePeriodicals +
                "\nПериод издательства: " + periodPublishing;
    }

}



package Java4;

import java.util.ArrayList;

public class AllFile {

    private ArrayList<Literature> fileOfLiterature;
    public AllFile(ArrayList<Literature> ListOfLiterature){
        this.fileOfLiterature = ListOfLiterature;
    }

    public void addLiterature(Literature literature){
        fileOfLiterature.add(literature);
    }

    public ArrayList<Literature> ToLiterature(){
        return fileOfLiterature;
    }

}

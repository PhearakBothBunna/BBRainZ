
import java.util.ArrayList;

public class Course implements Comparable {


    private String fullName;
    private int number;
    private ArrayList<ArrayList<Integer>> preReqs;

    public Course(int number, String fullName, ArrayList<ArrayList<Integer>> preReqs){
        this.fullName = fullName;
        this.number = number;
        this.preReqs = preReqs;
    }

    public int getNumber(){
        return number;
    }

    public String getFullName(){
        return fullName;
    }
    
    public ArrayList<ArrayList<Integer>> getPreReqs(){
        return preReqs;
    }

    @Override
    public int compareTo(Object obj) {
        if(this.number > (int)(obj)){
            return 1;
        }
        else{
            return 0;
        }
    }

    public String toString(){
        return fullName;

    }

}

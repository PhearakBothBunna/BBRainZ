
import java.util.ArrayList;

public class Courses implements Comparable {

    private final String name;
    private final int number;
    private final ArrayList<String> preReqs;

    public Courses(String name, int number, ArrayList<String> preReqs){
        this.name = name;
        this.number = number;
        this.preReqs = preReqs;
    }

    public void addCourse(String courseName){
        preReqs.add(courseName);
    }

    public void rmCourse (String courseName) {
        preReqs.remove(courseName);
    }

    public int getNumber(){
        return number;
    }

    public String getName() {
        return name;
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

}


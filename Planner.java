import java.util.ArrayList;
import java.util.Collections;

public class Planner {

    // Array lists for each categories
    private final ArrayList <String> prevCourse ;
    private final ArrayList <String> currCourse;
    private final ArrayList <String> futureCourse;
    private final ArrayList <String> preReqMet ;
    private final ArrayList <String> preReqNotMet;

    public Planner (ArrayList<String> prevCourse, ArrayList<String> currCourse,
                    ArrayList <String> futureCourse, ArrayList<String> preReqMet,
                    ArrayList<String> preReqNotMet){

        this.prevCourse = prevCourse;
        this.currCourse = currCourse;
        this.futureCourse = futureCourse;
        this.preReqMet = preReqMet;
        this.preReqNotMet = preReqNotMet;
    }

    public void addCourse(ArrayList <String> courseType, String courseName){
        // Add the course to an arraylist
        courseType.add(courseName);
    }

    public void moveCourse(ArrayList <String> courseType, String courseName, ArrayList <String> toCourse){
        // Move a course from an arraylist to another arraylist
        courseType.remove(courseName);
        toCourse.add(courseName);
    }

    public ArrayList<String> getPrevCourse() {
        return prevCourse;
    }

    public ArrayList<String> getCurrCourse() {
        return currCourse;
    }

    public ArrayList<String> getFutureCourse() {
        return futureCourse;
    }

    public ArrayList<String> getPreReqMet() {
        return preReqMet;
    }

    public ArrayList<String> getPreReqNotMet() {
        return preReqNotMet;
    }

    // if there's at least 1 pre requisite class that we haven't taken,it will return false
    // which means that we cannot pick the class
    // true: can pick, false: can't pick
    public boolean canPickClass(){
        return preReqNotMet.size() < 1;
    }


    // Sort the arraylist
    public void sort(ArrayList<String> courseType) {
        Collections.sort(courseType);
    }
}

import java.util.ArrayList;
import java.util.Collections;

public class Planner {

    // Array lists for each categories
    private ArrayList<Course> takingCourses;
    private ArrayList<Course> preReqMet;
    private ArrayList<Course> preReqNotMet;

    public Planner(){
        this.takingCourses = new ArrayList<>();
        this.preReqMet = new ArrayList<>();
        this.preReqNotMet = new ArrayList<>();
    }

    public void addTakingCourse(Course newCourse){
        takingCourses.add(newCourse);
    }
    
    public void addPreReqMet(Course newCourse){
        preReqMet.add(newCourse);
    }
    
    public void addPreReqNotMet(Course newCourse){
        preReqNotMet.add(newCourse);
    }
    
    public void removeTakingCourse(Course newCourse){
        takingCourses.remove(newCourse);
    }
    
    public void removePreReqMet(Course newCourse){
        preReqMet.remove(newCourse);
    }
    
    public void removePreReqNotMet(Course newCourse){
        preReqNotMet.remove(newCourse);
    }
    
    public ArrayList<Boolean> preReqsMet(Course course){
        ArrayList<Boolean> temp = new ArrayList<>();
        for(ArrayList<Integer> preReqList : course.getPreReqs()){
            Boolean flag = false;
            for(int preReq: preReqList){
                if(takingCourses.contains(preReq)){
                     flag = true;
                }
            }
            temp.add(flag);
        }
        return temp;
    }
    
    public boolean addCourse(Course newCourse){
        ArrayList<Boolean> temp = preReqsMet(newCourse);
        if(temp.contains(false)){
            addPreReqNotMet(newCourse);
            return false;
        }
        else{
            addPreReqMet(newCourse);
            return true;
        }
    }

    public ArrayList<Course> getTakingCourses() {
        return takingCourses;
    }

    public ArrayList<Course> getPreReqMet() {
        return preReqMet;
    }

    public ArrayList<Course> getPreReqNotMet() {
        return preReqNotMet;
    }
}

public class Box{
  
  private String name;
  private Course course;
  private float x;
  private float y;
  private boolean overBox;
  private boolean locked;
  private boolean draggable;
  private boolean removable;
  private float xOffset; 
  private float yOffset;
  private color boxColor1;
  private color boxColor2;
  private int timer;
  
  Box(String name, Course course, boolean locked, color boxColor1, color boxColor2){
    this.name = name;
    this.course = course;
    this.x = random(100, 800);
    this.y = random(100, 800);
    this.overBox = false;
    this.locked = locked;
    this.draggable = false;
    this.removable = true;
    this.xOffset = 0.0;
    this.yOffset = 0.0;
    this.boxColor1 = boxColor1;
    this.boxColor2 = boxColor2;
    this.timer = 0;
  }
  
  public void setCoord(float newX, float newY){
    x = newX;
    y = newY;
  }
  
  public Course getCourse(){
    return course;
  }
  
  public boolean getOver(){
    return overBox;
  }
  
  public void setLocked(boolean locked){
    this.locked = locked;
  }
  
  public void display(){
    // Test if the cursor is over the box 
    if (mouseX > x-boxSizeX && mouseX < x+boxSizeX && 
        mouseY > y-boxSizeY && mouseY < y+boxSizeY) {
      overBox = true;
      timer ++;
      stroke(255); 
    } else {
      stroke(boxColor2);
      overBox = false;
      timer = 0;
    }
    
    // Draw the box
    fill(boxColor1);
    strokeWeight(5);
    rect(x, y, boxSizeX, boxSizeY, 20);
    textSize(22);
    fill(255);
    text(name, x,y+10);
    
  }
  
  public void myMousePressed(){
    if(overBox && !locked) { 
      draggable = true;
    } else {
      draggable = false;
    }
    xOffset = mouseX-x; 
    yOffset = mouseY-y;
    
    boolean flag = true;
    for(int i = 5; i < areas.size() && flag && !locked && removable; i++){
      int[] area = areas.get(i);
      if(x > area[0] && x < area[1] && 
         y > area[2] && y < area[3]){
         allBuckets.get(i).remove(this);
         if(i < 8){
           allSemesters.remove(this);
         }
         flag = false;
         removable = false;
      }
    }
  }
  
  public void myMouseDragged(){
    if(draggable && !locked) {
      x = mouseX-xOffset; 
      y = mouseY-yOffset; 
    }
  }
  
  public void myMouseReleased(){
    draggable = false;
    
    boolean flag = true;
    for(int i = 5; i < areas.size() && flag && !locked; i++){
      int[] area = areas.get(i);
      if(x > area[0] && x < area[1] && 
         y > area[2] && y < area[3]){
         allBuckets.get(i).add(this);
         if(i < 8){
           allSemesters.add(this);
         }
         flag = false;
         removable = true;
      }
    }
  }
  
  public void popup(){
    if(timer >= 60 && !draggable){
      noStroke();
      fill(220);
      rect(x+200, y, 120, 120, 20);
      textSize(35);
      fill(0);
      text("Pre-requisites:", x+200, y-70);
      textSize(25);
      int i = -30;
      for(ArrayList<Integer> prereqs : course.getPreReqs()){
        fill(0);
        text("CPT S ", x+120, y+i);
        for(int j = 0; j < prereqs.size(); j++){
          if(j > 0){
            textSize(20);
            fill(0);
            text("or", x + 150 + (60 * j), y + i);
          }
          if(myContains(prereqs.get(j))){
            fill(0, 200, 0);
          }
          else{
            fill(255, 0, 0);
          }
          textSize(25);
          text(prereqs.get(j), x + 180 + (60 * j), y + i);
        }
        i += 40;
      }
    }
  }
}

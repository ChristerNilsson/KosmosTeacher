void setup() {
    size(600,600);
}    

void draw(){
    background(0);
    fill(255,0,0);
    rect(0,0,10,10); // saved as 255,0,0
    
    stroke(255,0,0);
    for (int i=0; i<10; i++)
      for (int j=0; j<10; j++)
        point(10+i,30+j); // saved as 223,0,0
}    

void mousePressed() {
    color col = get(mouseX,mouseY);
    println(red(col),green(col),blue(col)); 
}    
 abstract class geometry{
	static float pi=3.14f;
	void printshape(){
		System.out.print("the shape is:");
}}
class circle extends geometry{
	int rad;
	circle(int rad){
		this.rad=rad;}
	void area(){
		System.out.println("area of circle:"+pi*rad*rad);
}
	void printer(){
		super.printshape();
		System.out.println("circle");}}
class inheritance{
	public static void main(String args[]){
		//geometry parent=new geometry();//geometry is an abstract class
		circle child=new circle(5);
		child.printer();
}}
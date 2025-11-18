interface geometry{
	double pi=3.14;//public static final(by default) 
	double area();//equivalent to->public abstract double pi=3.14;
	double perimeter();
}
class circle implements geometry {
	double rad;
	circle(double rad){
		this.rad=rad;}
	public double area(){
		return pi*rad*rad;}
	public double perimeter(){
		return 2*pi*rad;}
}
class interfaces2{
	public static void main(String args[]){
		circle c=new circle(3);
		geometry geo;//geometry geo=new geometry() throws error
		geo=c;
		System.out.println(geo.area());}}
	
		 
import java.lang.*;
class original implements Cloneable{
	int x;
	original(int x){
		this.x=x;}
	int square(int x){
		return x*x;}
	public Object clone(){
		return new original(this.x);}}
class clonable_interface{
public static void main(String args[]){
	original org=new original(255);
	original copy=(original)org.clone();
	System.out.println(copy.x);}}
	 
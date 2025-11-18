class finalclass{
	int x=2;}
public class finalex{
public static void main(String args[]){
	final finalclass myclass=new finalclass();
	myclass.x=3;//the internal members can be changed but not the object reference
	myclass=new finalclass();//this throws error
}}
	
interface structure{     //equivalent to "public abstract class structure" e
	int x=2;             //the variable are like "public static final type varname=value"     
	void printer();      //by default(if not explicitly given) the all the method are "public abstract"
	//The DEFAULT KEYWORD can be used to define the method body that is common to all the classes that implements
	//the interface
	default void commonMethod(){
		System.out.println("This is a default method");
	}
	//The static methods can also be defined
	static void theStaticMethod(){
		System.out.println("Don't have to implement and instantiate to call me"); 
	}
}  
class struct1 implements structure{
	int y=2;
	public void printer(){
		//System.out.println(y);
		System.out.println("printing");
	}
}
class interfaces{
	public static void main(String args[]){
		structure s = new struct1();
		s.printer();
		System.out.println(s.x);
		s.commonMethod();;
		structure.theStaticMethod();
	}
}	
/*the abstract class cant be instantiated, it just used to provide the frame work 
for the subclasses. the abstract method in the abstract or normal super class must be 
overridden its subclass. Thereby we ensure all the subclasses must contain the 
particular method. An abstract class can have both abstract and concrete method(method's body is defined within the
abstract class)*/
abstract class animal{
	abstract void sound();
	int concreteMethod(){
		return 2;
	}
}
class dog extends animal{
	void sound(){//if sound is not overriden then throws the error
		System.out.println("barking");
	}
}
class abstraction{
	public static void main(String args[]){
		animal mydog=new dog();
		mydog.sound();
		System.out.println(mydog.concreteMethod());
	}
}

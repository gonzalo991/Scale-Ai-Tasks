public interface IPlayable {
void play(String name);
}

public class Dog implements IAnimal, IPlayable{
private String breed;
private String color;
private String name;

public Dog(String breed, String color, String name) {
this.breed = breed;
this.color = color;
this.name = name;
}

public String getName() {
return name;
}

public void setName(String name) {
this.name = name;
}

public String getBreed() {
return breed;
}

public void setBreed(String breed) {
this.breed = breed;
}

public String getColor() {
return color;
}

public void setColor(String color) {
this.color = color;
}

@Override
public void run() {
System.out.println("The dog is running...");
}

@Override
public void walk() {
System.out.println("The dog is walking...");
}

@Override
public void eat(String name) {
System.out.println(name + " is eating...");
}

@Override
public void drink_water(String name) {
System.out.println(name + " is drinking water...");
}

@Override
public void sleep() {
System.out.println("The dog is sleeping...");
}

@Override
public void play(String name) {
System.out.println(name + " is playing...");
}
}

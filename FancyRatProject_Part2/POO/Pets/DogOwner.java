public class DogOwner {
private String name;
private String surname;
private Dog dog;

public DogOwner(){
}

public DogOwner(String name, String surname, Dog dog) {
this.name = name;
this.surname = surname;
this.dog = dog;
}

public String getName() {
return this.name;
}

public void setName(String name){
this.name = name;
}

public String getSurname(){
return this.surname;
}

public void setSurname(String surname){
this.surname = surname;
}

public Dog getDog() {
return this.dog;
}

public void setDog(Dog newDog) {
dog = newDog;
}

@Override
public String toString() {
return "DogOwner: "+ "[ name: " + this.name + " surname: "+this.surname+" [dog: " +
this.dog + "]";
}
}
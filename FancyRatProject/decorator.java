// Define the abstract component
abstract class Employee {
     protected String name;
     public Employee(String name){
          this.name = name;
      }
      public abstract String getName();
}

// Define the concrete component  
class AnEmployee extends Employee {
    public AnEmployee(String name) {
         super(name);
     }
     public String getName(){
          return name;
     }
}

// Define the base decorator
abstract class EmployeeDecorator extends Employee {
    protected Employee decoratedEmployee;

     public EmployeeDecorator(Employee decoratedEmployee){
         super(decoratedEmployee.getName());
         this.decoratedEmployee = decoratedEmployee;
      }

     public String getName(){
         return decoratedEmployee.getName();
     }
}

class Manager extends EmployeeDecorator {
    private List<Employee> employees;

    public Manager(Employee decoratedEmployee, List<Employee> employees) {
         super(decoratedEmployee);
         this.employees = employees;
       }

       @Override
       public String getName() {
            return decoratedEmployee.getName() + " is managing employees";
        }

        public List<Employee> getEmployees() {
            return employees;
        }
 }

// Define the client class
class Client {
  private List<Employee> employees;

  public Client(List<Employee> employees) {
    this.employees = employees;
  }

  public List<Employee> getEmployees() {
    return employees;
  }
}

// Use the classes
List<Employee> employees = new ArrayList<>();
employees.add(new AnEmployee("John"));
employees.add(new AnEmployee("Jane"));

Employee manager1 = new Manager(new AnEmployee("Michael"), employees);
Employee manager2 = new Manager(new AnEmployee("Rachel"), employees);

List<Employee> managers = new ArrayList<>();
managers.add(manager1);
managers.add(manager2);

Client client = new Client(managers);

System.out.println(client.getEmployees().get(0).getName()); // Output: Michael is managing employees
System.out.println(client.getEmployees().get(1).getName()); // Output: Rachel is managing employees
package Bridge_Java;
interface Implementador {
  void operacion();
}

class ImplementacionA implements Implementador {

  public void operacion() {
    System.out.println("Esta es la implementacion A");
  }
}

class ImplementacionB implements Implementador {

  public void operacion() {
    System.out.println("Esta es una implementacion de B");
  }
}

interface Abstraccion {
  void operacion();
}

class AbstraccionRefinada implements Abstraccion {

  private Implementador implementador;

  public AbstraccionRefinada(Implementador implementador) {
    this.implementador = implementador;
  }

  public void operacion() {
    implementador.operacion();
  }
}

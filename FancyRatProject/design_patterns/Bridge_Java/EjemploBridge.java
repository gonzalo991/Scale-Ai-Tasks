package Bridge_Java;

public class EjemploBridge {

  public static void main(String[] args) {
    Abstraccion[] abstracciones = new Abstraccion[2];
    abstracciones[0] = new AbstraccionRefinada(new ImplementacionA());
    abstracciones[1] = new AbstraccionRefinada(new ImplementacionB());
    for (Abstraccion abstraccion : abstracciones) abstraccion.operacion();
  }
}

package objetos.java.instrumentos;

public class Principal {
    public static Banda b = new Banda();
    public static void main(String[] args) {
        b.agregarMusico("Juan");
        b.agregarMusico("Maria");
        b.agregarMusico("Miguel");

        b.presentarBanda();
    }

    
}

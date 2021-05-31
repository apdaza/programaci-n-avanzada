package objetos.java.instrumentos;

public class Guitarra implements Instrumento {

    @Override
    public void afinar() {
        System.out.println("Afinando guitarra");

    }

    @Override
    public void tocar() {
        System.out.println("Tocando guitarra");

    }

    @Override
    public void tocar(String nota) {
        System.out.println("Tocando guitarra en " + nota);

    }
    
}

package objetos.java.instrumentos;

public class Bajo implements Instrumento{
    @Override
    public void afinar() {
        System.out.println("Afinando bajo");

    }

    @Override
    public void tocar() {
        System.out.println("Tocando bajo");

    }

    @Override
    public void tocar(String nota) {
        System.out.println("Tocando bajo en " + nota);

    }
}

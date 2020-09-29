package objetos.java.instrumentos;
import java.util.Random;

public class Principal {
    public static void main(String[] args) {
        Instrumento i;
        Random rn = new Random();

        int opc = rn.nextInt(3);

        switch(opc){
            case 1:
                i = new Guitarra();
                break;
            default:
                i = new Bajo();
                break;
        }

        i.afinar();
        i.tocar();
        i.tocar("DO");

    }

    
}

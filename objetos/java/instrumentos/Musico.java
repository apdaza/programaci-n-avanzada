package objetos.java.instrumentos;

public class Musico extends Persona{

    /* metodo polimorfico
       aplica sustitución de liskov (Instrumento -> (Guitarra, Bajo o Violin))
    */
    public void tocar(Instrumento i){
        i.afinar();
        i.tocar();
        i.tocar("Do");
    }
    
}

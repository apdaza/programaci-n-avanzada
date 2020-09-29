package objetos.java;

class Persona{
    private String nombre;
    private String apellido;

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public void setApellido(String apellido){
        this.apellido = apellido;
    }

    public String getNombre(){
        return this.nombre;
    }

    public String getApellido(){
        return this.apellido;
    }
}

class Saludador {
    private Persona p;

    public void setPersona(Persona p){
        this.p = p;
    }

    public String saludar(String msg){
        return msg + p.getNombre() + " " + p.getApellido();
    }
}

public class PrimerObjeto {
    public static void main(String[] args) {
        Persona p = new Persona();
        p.setNombre("Alejandro");
        p.setApellido("Daza");

        Saludador s = new Saludador();
        s.setPersona(p);
        System.out.println(s.saludar("Buen día "));
    }
    
}

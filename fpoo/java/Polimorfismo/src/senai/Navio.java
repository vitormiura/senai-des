package senai;

public class Navio extends Modal{
    public String porto;
    public String comandante;

    public Navio(String porto, String comandante, double carga, double velocidade){
        super(velocidade);
        this.cargaMaxima = 10000;
        this.porto = porto;
        this.comandante = comandante;
        verificaCarga(carga);
    }
}

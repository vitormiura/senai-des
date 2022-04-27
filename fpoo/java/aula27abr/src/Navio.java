public class Navio extends Modal{
    public String porto;
    public String comandante;

    public Navio(String porto, String comandante, double velocidade, double cargaAtual) {
        super(velocidade);
        this.cargaMaxima = 2500;
        System.out.println("caravela de judas");
        this.porto = porto;
        this.comandante = comandante;
        verificaCarga(cargaAtual);
    }

    @Override
    public String toString() {
        return "Navio{" +
                "combustivel='" + combustivel + '\'' +
                ", cargaMaxima=" + cargaMaxima +
                ", velocidade=" + velocidade +
                ", valorFrete=" + valorFrete +
                ", porto='" + porto + '\'' +
                ", comandante='" + comandante + '\'' +
                '}';
    }
}

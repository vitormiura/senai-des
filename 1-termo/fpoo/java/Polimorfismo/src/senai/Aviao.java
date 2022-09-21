package senai;

public abstract class Aviao extends Modal {
    public String aeroporto;
    public String modelo;
    public String piloto;
    public int qtdTurbina;

    public Aviao(String aeroporto, String modelo, String piloto, double cargaAtual,int qtdTurbina) {
        this.cargaMaxima = 3000;
        this.aeroporto = aeroporto;
        this.modelo = modelo;
        this.piloto = piloto;
        this.qtdTurbina = qtdTurbina;
        verificaCarga(cargaAtual);
        calcularVelocidade();
    }

    @Override
    public void calcularVelocidade(){
        this.velocidade = 300 * this.qtdTurbina;
    }

    @Override
    public String toString() {
        return "Aviao{" +
                "aeroporto='" + aeroporto + '\'' +
                ", modelo='" + modelo + '\'' +
                ", piloto='" + piloto + '\'' +
                ", combustivel='" + combustivel + '\'' +
                ", cargaMaxima=" + cargaMaxima +
                ", velocidade=" + velocidade +
                ", valorFrete=" + valorFrete +
                '}';
    }
}


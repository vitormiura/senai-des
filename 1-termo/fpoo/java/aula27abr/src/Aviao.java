public class Aviao extends Modal{
    public String aeroporto;
    public String modelo;
    public String piloto;
    public int qtdTurbina;

    public Aviao(String aeroporto, String modelo, String piloto, double cargaAtual, int qtdTurbina){
        this.cargaMaxima = 1000;
        System.out.println("aviao malasia que cai!");
        this.aeroporto = aeroporto;
        this.modelo = modelo;
        this.piloto = piloto;
        this.qtdTurbina = qtdTurbina;

        verificaCarga(cargaAtual);
        calcularVelocidade();
    }

    @Override
    public void calcularFrete() {

    }

    @Override
    public void calcularVelocidade() {
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

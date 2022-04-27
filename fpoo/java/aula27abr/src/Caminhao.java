public class Caminhao extends Modal{
    public String garagem;
    public int eixos;
    public String motorista;

    public Caminhao() {
        System.out.println("caminhao marabraz");
    }

    public void definirCaminhao(String garagem, int eixos, String motorista){
        this.garagem = garagem;
        this.eixos = eixos;
        this.motorista = motorista;

        if (eixos > 30)
            throw new IllegalArgumentException();
        this.eixos = eixos;

        calcEixos(this.eixos);
        calcularVelocidade();

    }

    public void calcEixos(int eixos){
        //4 eixos = 1 ton
        this.cargaMaxima = 250 * eixos;
    }

    @Override
    public String toString() {
        return "Caminhao{" +
                "garagem='" + garagem + '\'' +
                ", eixos=" + eixos +
                ", motorista='" + motorista + '\'' +
                ", combustivel='" + combustivel + '\'' +
                ", cargaMaxima=" + cargaMaxima +
                ", velocidade=" + velocidade +
                ", valorFrete=" + valorFrete +
                '}';
    }
}

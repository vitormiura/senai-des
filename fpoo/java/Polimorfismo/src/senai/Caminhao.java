package senai;

public abstract class Caminhao extends Modal{
    public String garagem;
    public int eixos;
    public String motorista;

    public Caminhao(){

    }

    public void definirCaminhao(String garagem, int eixos, String motorista){
        this.garagem = garagem;
        this.motorista = motorista;

        if (eixos > 30)
            throw new IllegalArgumentException("Caminhão de marte");
            this.eixos = eixos;
        calcEixos(this.eixos);
    }

    public void calcEixos(int eixos){
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

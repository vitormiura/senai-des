package senai;

public abstract class Modal {
    public String combustivel;
    public double cargaMaxima;
    public double velocidade;
    public double valorFrete;
    private boolean carregado;

    public boolean isCarregado() {
        return carregado;
    }

    public void setCarregado(boolean carregado) {
        this.carregado = carregado;
    }

    public void verificaCarga(double cargaAtual){
        if (cargaMaxima - (cargaMaxima * 0.2 ) <= cargaAtual) {
            System.out.println("Carregado");
            this.carregado = true;
        }
        else{
            System.out.println("Não carregado");
            this.carregado = false;
        }
    }
    public void calcularVelocidade(){
        double velocidadeInicial = 20;
        double kgVelocidade = 250;

        this.velocidade = (cargaMaxima / kgVelocidade) * velocidadeInicial;
    }

    public abstract void calcularFrete();


    public  Modal(double velocidade){
        this.velocidade = velocidade;
    }
    public Modal(){}

}

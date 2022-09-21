public abstract class Modal {
    public String combustivel;
    public double cargaMaxima;
    public double velocidade;
    private boolean carregado;
    public double valorFrete;
    private String novaVariavel;


    //OVERLOAD
    public Modal(){

    }

    public Modal(double velocidade){
        this.velocidade = velocidade;
    }

    public void calcularFrete(){

    }

    public void calcularVelocidade(){
        double veloInicial = 20;
        double kgVelocidade = 250;
        System.out.println(veloInicial);

        this.velocidade = ((cargaMaxima / kgVelocidade) * veloInicial/10);

    }

    public boolean isCarregado() {
        return carregado;
    }

    public void setCarregado(boolean carregado) {
        this.carregado = carregado;
    }
    //metodo para verificar carga do aviao
    //se carga atual for . 80% entao carregado = true
    public void verificaCarga(double cargaAtual){
        if(cargaMaxima - (cargaMaxima * 0.2) <= cargaAtual){
            this.carregado = true;
        }else{
            this.carregado = false;
        }
    }
}

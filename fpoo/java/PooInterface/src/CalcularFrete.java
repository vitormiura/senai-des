public class CalcularFrete implements Calcular{
    public double distancia;
    public double valorFrete;


    public CalcularFrete(double distancia){
        this.distancia = distancia;
    }

    public CalcularFrete(){

    }

    public double calcular(){
        return distancia * 0.5;
    }

    public double calcF(){

        double valorDis = distancia * 0.5;
        double valorPneu = calcDesgastePneus();
        double comb = calcCombustivel();
        double oleo = calcOleo();
        

        return this.calcICMS(valorDis, valorPneu, comb, oleo
        );
    }

    public double calcICMS(double valorFrete){
        //taxa de 20%
        return valorFrete += valorFrete * 0.2;
    }

    @Override
    public double calcCombustivel() {
        
        return distancia * 8;
    }

    @Override
    public double calcICMS() {
        
        return distancia * 100;
    }

    @Override
    public double calcIPI() {

        return distancia * 0.5;
    }

    @Override
    public double calcDesgastePneus() {
        return distancia * 0.1;
    }

    @Override
    public double calcOleo() {

        return distancia * 0.2;
    }

}

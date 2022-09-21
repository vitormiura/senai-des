public class RelatorioFrete extends CalcularFrete {

    private CalcularFrete frete;

    public RelatorioFrete(CalcularFrete frete){
        this.frete = frete;
    }

    public void printFrete(){
        System.out.println(frete.calcF());
    }

    public void printFrete(double distancia){
        System.out.println("carga pesada");
        CalcularFrete calc1 = new CalcularFrete(distancia);
        System.out.println(calc1.calcular());
        System.out.println(calc1.calcCombustivel());
    }
}

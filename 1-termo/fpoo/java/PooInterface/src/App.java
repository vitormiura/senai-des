import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Digite a distancia: ");
        double dist = new Scanner(System.in).nextDouble();
        CalcularFrete calculo1 = new CalcularFrete(dist);
        //System.out.println(calculo1.calcular());


        RelatorioFrete rel = new RelatorioFrete(calculo1);
        rel.printFrete();
        //rel.distancia = dist;
        //rel.printFrete(dist);

    }
}

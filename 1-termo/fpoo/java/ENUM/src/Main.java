import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {

        System.out.println(Mensagens.BemVindo.getMsg());

        System.out.println("Digite " + Opcoes.SIM.ordinal() + " para " + Opcoes.SIM + " e " + Opcoes.NAO.ordinal() + " para " + Opcoes.NAO + ": ");
        Scanner input = new Scanner(System.in);
        int op = input.nextInt();

        if (op == Opcoes.SIM.getVal()){
            System.out.println("Escolheu SIM");
        }else if (op == Opcoes.NAO.getVal()){
            System.out.println("Escolheu NAO");
        }else{
            System.out.println("Talvez");
        }

        //System.out.println(Opcoes.NAO.ordinal());


        //Thread.sleep(1000);

        //System.out.println(Mensagens.Saiu.getMsg());
    }
}

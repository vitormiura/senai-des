import java.io.IOException;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        // BURRICE ABAIXO
        // ArrayList<String> oi = new ArrayList<>();

        // Scanner input = new Scanner(System.in);
        // System.out.println("Digite o nome do arquivo: ");
        // String haha = input.nextLine();
        // System.out.println("Digite o tamanho de elementos: ");
        // int num = input.nextInt();

        // for (int i=0;i<num+1;i++) {
        //     System.out.println("digite elementos da lista:");
        //     oi.add(input.nextLine());
        // }

        // System.out.println(EscreverTxt.tamanhoLista);
        // EscreverTxt.gravarTxt(haha, oi);

        EscreverTxt novotxt = new EscreverTxt();
        while(true){
            
            LocalDateTime hora = LocalDateTime.now();
            ArrayList<String> lista = new ArrayList<String>();
            ArrayList<String> log = new ArrayList<String>();
            Scanner input = new Scanner(System.in);
            System.out.println("Digite seu nome:");
            String nome = input.nextLine();

            while (true){
                System.out.println("Digite seus produtos (oi para sair)");
                String txtDigitado = input.nextLine();
                if(txtDigitado.equals("oi"))
                    break;
                lista.add(txtDigitado);
                //log.add("Pedido " + nome + " Adicionou " + txtDigitado + " as " + agora);
            }
            //System.out.println(lista);
            novotxt.gravarTxt(nome, lista);
            log.add("Pedido " + nome + " adicionado " + lista + " as " + hora);
            novotxt.log(log);

            Thread.sleep(1000);

            novotxt.letTxt(nome);
            System.out.println("Deseja criar um novo pedido? (s/n)");
            String op = input.nextLine();
            if(op.equals("n"))
                
                break;
        }
    }
}

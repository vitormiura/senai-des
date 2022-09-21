import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Gravar write = new Gravar();
        Scanner input = new Scanner(System.in);
        ArrayList<String> coluna = new ArrayList<>();
        ArrayList<String> linhas = new ArrayList<>();

        while(true){
            System.out.println("Digite o nome da coluna: ");
            //while(input.hasNextLine()){
            String i = input.nextLine();
            coluna.add(i);
            //} 
            System.out.println("Deseja adicionar outra?");
            String op = input.nextLine();
            if (op.equals("s")){
                continue;
            }else{
                break;
            }
        }   
        write.salvarCsv(list);

        while(true){
            System.out.println("a");
        }
        
        //write.salvarCsv();
        input.close();
    }
}

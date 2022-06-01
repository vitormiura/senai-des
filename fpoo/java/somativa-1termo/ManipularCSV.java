import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ManipularCSV {

    public void lerCSVBuffer() throws IOException {
        List<List<String>> registros = new ArrayList<>();
        BufferedReader leitorCSV = new BufferedReader(new FileReader("alunos.csv"));
        String linha;
        while ((linha = leitorCSV.readLine()) != null) {
            String[] dados = linha.split(",");
            registros.add(List.of(dados));
        }
        leitorCSV.close();
        System.out.println(registros);
    }
}

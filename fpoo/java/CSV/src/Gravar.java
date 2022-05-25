import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

public class Gravar {
    ArrayList<String> lista = new ArrayList<>();

    public void salvarCsv(ArrayList<String> lista) throws IOException{
        // lista.add("Nome,idade,peso");
        // lista.add("Vitor,100,100");
        Path path = Paths.get("dados.csv");
        Files.write(path, lista, StandardCharsets.UTF_8);
    
    }
    public void lerCsv() throws IOException{
        Path path = Paths.get("dados.csv");
        String data = new String(String.valueOf(Files.readAllLines(path)));
        System.out.println(data);
    }

    public void addColuna(ArrayList<String> lista) throws IOException{
        Path path = Paths.get("dados.csv");
        Files.write(path, lista, StandardCharsets.UTF_8);
    }
}

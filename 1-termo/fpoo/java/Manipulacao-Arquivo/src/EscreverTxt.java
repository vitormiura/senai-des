import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
//import java.time.LocalDateTime;
import java.util.List;

public class EscreverTxt {
    private String nome;
    private List<String> lista;
    public static int tamanhoLista;

    public void gravarTxt(String nome, List<String> lista) throws IOException {
        Path caminho = Paths.get(nome + ".txt");
        //System.out.println(lista);
        Files.write(caminho, lista, StandardCharsets.UTF_8);
    }
    public void letTxt(String nomeArquivo) throws IOException{
        Path caminho = Paths.get(nomeArquivo + ".txt");
        String data = new String(String.valueOf(Files.readAllLines(caminho)));
        System.out.println(data);
    }
    public void log(List<String> oi) throws IOException{
        Path c = Paths.get("log.txt");
        if(Files.readAllLines(c) != null){
            System.out.println("\n");
            Files.write(c, oi, StandardCharsets.UTF_8, StandardOpenOption.APPEND);
        }else{
            Files.write(c, oi, StandardCharsets.UTF_8);   
        }
    // public void logApp(List<String> oi) throws IOException{
    //     Path c = Paths.get("log.txt");
    //     if(Files.readAllLines(c) != null){
    //         System.out.println("\n");
    //         Files.write(c, oi, StandardCharsets.UTF_8, StandardOpenOption.APPEND);
    //     }else{
    //         Files.write(c, oi, StandardCharsets.UTF_8);   
    //     }
    }
}

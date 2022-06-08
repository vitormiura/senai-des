import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

public class Log{
    public static void log(String oi) throws IOException{
        String file = "Log.txt";
        ArrayList<String> ois = new ArrayList<String>();
        ois.add(oi);
        Path c = Paths.get(file.toString());

        Files.write(c, ois, StandardCharsets.UTF_8, StandardOpenOption.APPEND);
   
    }
}

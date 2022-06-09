import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args) throws Exception {
        LocalDateTime hour = LocalDateTime.now();
        new Login();
        Log.log("["+ hour + "]" + " system init.");
    }
}

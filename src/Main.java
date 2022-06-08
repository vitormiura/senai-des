import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args) throws Exception {
        LocalDateTime hora = LocalDateTime.now();
        new Login();
        Log.log("("+ hora + ")" + " user logged in.");
    }
}

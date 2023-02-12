import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.nio.file.*;
import java.time.LocalDateTime;
import static java.nio.file.StandardOpenOption.*;

public class Login extends JFrame {
    JTextField login;
    JTextField pass;
    JButton ok, cad;
    String file = "Users.txt";
    LocalDateTime hour = LocalDateTime.now();

    public Login() {
        super("Login - Estoque Brabo");

        login = new JTextField();
        pass = new JTextField();
        ok = new JButton("Sign In");
        ok.addActionListener(new signin());
        cad = new JButton("Sign Up");
        cad.addActionListener(new signup());

        Container cont = getContentPane();
        cont.setLayout(new GridLayout(3, 2));
        cont.add(new JLabel("Login:"));
        cont.add(login);
        cont.add(new JLabel("Senha:"));
        cont.add(pass);
        cont.add(ok);
        cont.add(cad);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 200);
        setVisible(true);
    }

    class signin implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            try {
                Path path = Paths.get(file.toString());
                InputStream input = Files.newInputStream(path);
                BufferedReader reader = new BufferedReader(new InputStreamReader(input));
                String temp = null;
                String user;
                String password;
                boolean auth = false;
                while((temp = reader.readLine()) != null){
                    String[] account = temp.split(",");
                    user = account[0];
                    password = account[1];

                    if(user.equals(login.getText()) && password.equals(pass.getText())){
                        auth = true;
                        Log.log("["+ hour + "] " + login.getText() +" logged in.");
                    }
                }
                if(auth == true){
                    new Window();
                    Log.log("["+ hour + "] " + login.getText() +" initialized inventory program.");
                    //this.dispose(); professor nao funcionou de nenhum jeito mandar essa janela embora
                }else{JOptionPane.showMessageDialog(null, "User not found!",
                "Error!", JOptionPane.ERROR_MESSAGE);}
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
            }
        }
    }

    class signup implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            try {
                Path path = Paths.get(file.toString());
                OutputStream output = new BufferedOutputStream(Files.newOutputStream(path, APPEND));
                BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(output));
                writer.write(login.getText() + "," + pass.getText());
                writer.newLine();
                JOptionPane.showMessageDialog(null, "Signup Successfully!");
                Log.log("["+ hour + "] " + login.getText() + " signed up.");
                writer.close();
                output.close(); 
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
            }
        }
    }
}

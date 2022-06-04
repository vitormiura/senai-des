import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Login extends JFrame {
    JTextField login;
    JPasswordField senha;
    JButton ok, cad;

    public Login() {
        super("Login - Estoque Brabo");

        login = new JTextField();
        senha = new JPasswordField();
        ok = new JButton("Sign In");
        ok.addActionListener(new signin());
        cad = new JButton("Sign Up");
        cad.addActionListener(new signup());

        Container cont = getContentPane();
        cont.setLayout(new GridLayout(3, 2));
        cont.add(new JLabel("Login:"));
        cont.add(login);
        cont.add(new JLabel("Senha:"));
        cont.add(senha);
        cont.add(ok);
        cont.add(cad);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 200);
        setVisible(true);
    }

    class signin implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            System.out.printf("Logado!");
            if (e.getSource() == ok) {
                new Window();
                //this.dispose();
            }
        }
    }

    class signup implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            login.setText("");
            senha.setText("");
            JOptionPane.showMessageDialog(null, "Dados limpos com Sucesso!");
        }
    }
}

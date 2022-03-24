import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class CalculadoraModelo1 extends JFrame implements ActionListener{

    public static void main(String[] args) {
        new CalculadoraModelo1();

    }

    JTextField display;
    String valorTxt;
    ArrayList<Double> listaNumeros;
    ArrayList<Character> listaCaracteres;
    double resultado;

    public CalculadoraModelo1(){
        super("Calculadora");

        listaNumeros = new ArrayList<Double>();
        listaCaracteres = new ArrayList<Character>();
        valorTxt = "";

        Container n = new JPanel();
        n.setLayout(new GridLayout(4,4));

        JButton btn7 = new JButton("7");
        btn7.addActionListener(this);
        n.add(btn7);
        JButton btn8 = new JButton("8");
        btn8.addActionListener(this);
        n.add(btn8);
        JButton btn9 = new JButton("9");
        btn9.addActionListener(this);
        n.add(btn9);
        JButton div = new JButton("/");
        div.addActionListener(this);
        n.add(div);
        JButton btn4 = new JButton("4");
        btn4.addActionListener(this);
        n.add(btn4);
        JButton btn5 = new JButton("5");
        btn5.addActionListener(this);
        n.add(btn5);
        JButton btn6 = new JButton("6");
        btn6.addActionListener(this);
        n.add(btn6);
        JButton mult = new JButton("*");
        mult.addActionListener(this);
        n.add(mult);
        JButton btn1 = new JButton("1");
        btn1.addActionListener(this);
        n.add(btn1);
        JButton btn2 = new JButton("2");
        btn2.addActionListener(this);
        n.add(btn2);
        JButton btn3 = new JButton("3");
        btn3.addActionListener(this);
        n.add(btn3);
        JButton minus = new JButton("-");
        minus.addActionListener(this);
        n.add(minus);
        JButton btn0 = new JButton("0");
        btn0.addActionListener(this);
        n.add(btn0);
        JButton dot = new JButton(".");
        dot.addActionListener(this);
        n.add(dot);
        JButton equal = new JButton("=");
        equal.addActionListener(this);
        n.add(equal);
        JButton plus = new JButton("+");
        plus.addActionListener(this);
        n.add(plus);

        Container c = getContentPane();

        display = new JTextField();
        display.setEditable(false);
        c.add(BorderLayout.NORTH, display);
        c.add(BorderLayout.CENTER, n);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 300);
        setVisible(true);
    }

    public boolean testarNumero(String numero){
        try{
            double numeroReal = Double.parseDouble(numero);
            return true;
        }catch(NumberFormatException exp){
            return false;
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String textoBotao = e.getActionCommand();
        // String textoBotao2 = ((JButton) e.getSource()).getText(); Metodo usando Cast
        valorTxt += textoBotao;

        double numero = 0.0;

        if(testarNumero(textoBotao)){
            numero = Double.parseDouble(textoBotao);
            display.setText(valorTxt);
            listaNumeros.add(numero);
            System.out.println(listaNumeros);

        }else{
            if(textoBotao == "="){
                calcular();
            }
            listaCaracteres.add(textoBotao.charAt(0));
            display.setText(display.getText() + textoBotao);
            display.setText(valorTxt);
        }

    }

    public double calcular(){
        double numero1, numero2;
        char operador;

        for (int i = 0; i<listaNumeros.size() - 1; i++) {
            numero1 = listaNumeros.get(i);
            numero2 = listaNumeros.get(i + 1);
            operador = listaCaracteres.get(i);

            System.out.println("Valor 1: " + numero1 + "Valor 2: " + numero2 + "Operador: " + operador);

        }
        
    return 0.00;
    }
}

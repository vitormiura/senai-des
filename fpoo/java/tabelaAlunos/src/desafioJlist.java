import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class desafioJlist extends JFrame implements ActionListener{

    JList <String> listaLinguagens;
    JList <String> listaConhecimento;
    DefaultListModel<String> listaInicial;
    DefaultListModel<String> listaEscolhas;

    public desafioJlist() {
        super("Lista de linguagens");

        Container painel = new JPanel();
        Container painelListas = new JPanel();
        Container botoes = new JPanel();
        Container conteudo = getContentPane();

        painel.setLayout(new FlowLayout());
        painelListas.setLayout(new GridLayout());
//        GridBagConstraints constraints = new GridBagConstraints();
//        constraints.insets = new Insets(10, 15 , 10, 15);
//        botoes.setLayout(new GridBagLayout(2, 1, 1,5));
        JLabel descritivo = new JLabel("Escolha as Linguagens preferidas", SwingConstants.CENTER);
        descritivo.setPreferredSize(new Dimension(400, 50));

        JButton resetar = new JButton("Resetar");
        resetar.setPreferredSize(new Dimension(100,50));
        resetar.addActionListener(this);

        JButton botaoAdd = new JButton(">>");
        botaoAdd.setPreferredSize(new Dimension(100,20));
        botaoAdd.addActionListener(this);

        JButton botaoRemover = new JButton("<<");
        botaoRemover.setPreferredSize(new Dimension(100,20));
        botaoRemover.addActionListener(this);

        botoes.add(botaoAdd, BorderLayout.SOUTH);
        botoes.add(botaoRemover, BorderLayout.NORTH);

        listaInicial = new DefaultListModel<>();
        listaEscolhas = new DefaultListModel<>();

        listaLinguagens = new JList<>(listaInicial);
        listaLinguagens.setBackground(Color.GRAY);

        listaConhecimento = new JList<>(listaEscolhas);
        listaConhecimento.setBackground(Color.GREEN);

        carregarLista();

        listaLinguagens.setBounds(250,100,75,75);
        listaLinguagens.setPreferredSize(new Dimension(200,200));
        listaConhecimento.setBounds(250,100,75,75);
        listaConhecimento.setPreferredSize(new Dimension(200,200));

        painel.add(descritivo);
        painelListas.add(listaLinguagens);
        painelListas.add(botoes);
        painelListas.add(listaConhecimento);
        painel.add(painelListas);
        painel.add(resetar);


        conteudo.add(painel);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setSize(800,500);
        setVisible(true);

    }

    private void carregarLista() {

        listaEscolhas.removeAllElements();
        listaInicial.removeAllElements();
        listaInicial.addElement("C#");
        listaInicial.addElement("Elixir");
        listaInicial.addElement("C++");
        listaInicial.addElement("Assembly");
        listaInicial.addElement("Python");
        listaInicial.addElement("Java");
        listaInicial.addElement("HTML");

    }

    public static void main(String[] args) {
        new desafioJlist();
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if (e.getActionCommand() == ">>") {
            if(listaLinguagens.getSelectedIndex() == -1){
                JOptionPane.showMessageDialog(null,"Por favor selevione uma linguagem");
        }else{
            listaEscolhas.addElement(listaLinguagens.getSelectedValue());
            listaInicial.remove(listaLinguagens.getSelectedIndex());
        }
    }
    else if(e.getActionCommand() == "<<"){
        if(listaConhecimento.getSelectedIndex() == -1){
            JOptionPane.showMessageDialog(null,"Por favor selecione uma linguagem");
        }
    else{
        listaInicial.addElement(listaConhecimento.getSelectedValue());
        listaEscolhas.remove(listaConhecimento.getSelectedIndex());
        }
    }else if(e.getActionCommand() == "Resetar"){
        if(listaLinguagens.getSelectedIndex() == 1){
            JOptionPane.showMessageDialog(null,"Verifique se possui linguagens no campo!");
        }else{
            carregarLista();
        }
    }    
}
}


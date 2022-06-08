import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.nio.file.*;
import java.time.LocalDateTime;
import java.util.ArrayList;

public class Window extends JFrame {
    String file = "Stock.txt";
    LocalDateTime hora = LocalDateTime.now();

    public Window() throws IOException{
        super("Storage Management");
        Container panel = new JPanel();

        panel.setPreferredSize(new Dimension(300, 300));

        Path path = Paths.get(file.toString());
        InputStream input = Files.newInputStream(path);
        BufferedReader reader = new BufferedReader(new InputStreamReader(input));

        String temp = null;
        ArrayList<String[]> tableArr = new ArrayList<>();
    
        int aux = 0;
        while((temp = reader.readLine()) != null){
            String[] table = temp.split(" ");
            aux += 1;
            tableArr.add(table);
        }

        String products[][] = new String[aux][4];

        temp = reader.readLine();
        for(int i = 0; i<tableArr.size(); i++){
            for(int x = 0; x<aux;x++){
                int contador = 0;
                String[] vetorAux = tableArr.get(x);
                for(int z = 0; z<=3; z++){
                    if(contador>3){
                        contador -= 1;
                    }
                    products[x][contador] = vetorAux[contador];
                    contador+=1;
                }
            }
        }

        String cols[] = { "ID", "Products", "Price", "Quantity" };

        DefaultTableModel model = new DefaultTableModel(products, cols);
        JTable table = new JTable(model);

        table.setSelectionMode(javax.swing.ListSelectionModel.SINGLE_SELECTION);

        table.setBounds(30, 40, 200, 100);

        JScrollPane scrollPainel = new JScrollPane(table);
        panel.add(scrollPainel);

        Container cont = getContentPane();
        cont.add(panel);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600, 620);
        setVisible(true);

        JButton addButton = new JButton("New Product");
        addButton.setPreferredSize(new Dimension(150, 50));

        JButton rmvButton = new JButton("Remove Product");
        rmvButton.setPreferredSize(new Dimension(150, 50));

        JButton svButton = new JButton("Save Inventory");
        svButton.setPreferredSize(new Dimension(150, 50));

        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                model.addRow(new Object[] { "", "", "", "" });
            }
        });

        rmvButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (table.getSelectedRow() != -1) {
                    model.removeRow(table.getSelectedRow());
                    JOptionPane.showMessageDialog(null, "Selected row deleted successfully");
                } else {
                    JOptionPane.showMessageDialog(null, "User not found!",
                            "Error!", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        svButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try{
                    String filepath = "Stock.txt";
                    File file = new File(filepath);
                    FileWriter fw = new FileWriter(file.getAbsoluteFile());
                    BufferedWriter bw = new BufferedWriter(fw);

                    for(int i = 0; i < table.getRowCount(); i++) {
                        for(int j = 0; j < table.getColumnCount(); j++) {
                            bw.write((String)table.getModel().getValueAt(i, j)+" ");
                        }
                        bw.write("\n");
                    }
                    bw.close();
                    fw.close();
                    JOptionPane.showMessageDialog(null, "Inventory saved successfully!");
                }catch (Exception ex) {
                    ex.printStackTrace();
                }
            }
        });
        panel.add(addButton);
        panel.add(rmvButton);
        panel.add(svButton);
    }

    public static void main(String[] args) throws IOException {
        new Window();
    }
}

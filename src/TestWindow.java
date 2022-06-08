import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class TestWindow extends JFrame {
    String path = "Stock.txt";

    public TestWindow() {
        super("Storage Management");

        Container panel = new JPanel();
        panel.setPreferredSize(new Dimension(300, 300));

        String products[][] = {
                { "1", "Furadeira", "150.50", "10000" },
                { "2", "Martelo", "25.45", "240124" },
                { "3", "Luva", "10", "12321321" }
        };


        //File file = new File(path);

        // try {
        //     BufferedReader br = new BufferedReader(new FileReader(file));
        //     Object[] lines = br.lines().toArray();

        //     for(int i=0; i<lines.length;i++){
        //         String line = lines[i].toString().trim();
        //         String[] dataRow = line.split(",");
        //         model.addRow(dataRow);
        //     }

        // } catch (FileNotFoundException e1) {
        //     e1.printStackTrace();
        // }
        
        // BufferedReader br = new BufferedReader(new FileReader(file));
        // Object[] lines = br.lines().toArray();

        // for(int i=0; i<lines.length;i++){
        //     String line = lines[i].toString().trim();
        //     String[] dataRow = line.split(",");
        //     products.addRow(dataRow);
        // }

        //String products[][] = {};
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
        setSize(600, 600);
        setVisible(true);

        JButton addButton = new JButton("New Product");
        addButton.setPreferredSize(new Dimension(150, 50));

        JButton rmvButton = new JButton("Remove Product");
        rmvButton.setPreferredSize(new Dimension(150, 50));

        JButton svButton = new JButton("Remove Product");
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
                    System.out.println("oi");
                }
            }
        });
        panel.add(addButton);
        panel.add(rmvButton);
        panel.add(svButton);
    }

    public static void main(String[] args) {
        new TestWindow();
    }
}

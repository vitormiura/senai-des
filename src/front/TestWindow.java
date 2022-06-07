package front;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TestWindow extends JFrame {
    DefaultTableModel model;

    public TestWindow() {
        super("Estoque Brabo");

        Container panel = new JPanel();
        panel.setPreferredSize(new Dimension(300, 300));

        String products[][] = {
                { "1", "Furadeira", "150.50", "10000" },
                { "2", "Martelo", "25.45", "240124" },
                { "3", "Luva", "10", "12321321" }
        };

        String cols[] = { "ID", "Products", "Price", "Quantity" };

        model = new DefaultTableModel(products, cols);
        JTable table = new JTable(model);

        // model.addRow(new Object[] { "1", "Furadeira", "150.10", "19999" });

        table.setSelectionMode(javax.swing.ListSelectionModel.SINGLE_SELECTION);

        // JTable row = new JTable(products, cols);

        // row.setDefaultEditor(Object.class, null);
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

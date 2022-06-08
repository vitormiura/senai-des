package windows;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.table.*;

public class Window extends JFrame {
   private JTable table;
   private DefaultTableModel model;
   private Object[][] data;
   private String[] columnNames;

   public Window() {
      super("Stock Control");

      Container panel = new JPanel();
      panel.setPreferredSize(new Dimension(300, 300));

      data = new Object[][] { { "101", "Martelo", "100", "10000" }, { "102", "Macaco", "130", "123" } };

      columnNames = new String[] { "ID", "Product", "Price", "Quantity" };

      model = new DefaultTableModel(data, columnNames);
      table = new JTable(model);

      table.setSelectionMode(javax.swing.ListSelectionModel.SINGLE_SELECTION);

      table.setBounds(30, 40, 200, 100);

      JScrollPane scrollPainel = new JScrollPane(table);
      panel.add(scrollPainel);

      Container cont = getContentPane();
      cont.add(panel);
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setSize(600, 600);
      setVisible(true);

      JButton addButton = new JButton("New product");
      addButton.setPreferredSize(new Dimension(150, 50));

      JButton rmvButton = new JButton("Remove product");
      rmvButton.setPreferredSize(new Dimension(150, 50));

      JButton svButton = new JButton("Save");
      svButton.setPreferredSize(new Dimension(150, 50));

      addButton.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent ae) {
            model.addRow(new Object[] { "", "", "", "" });
         }
      });

      rmvButton.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent ae) {
            if (table.getSelectedRow() != -1) {
               model.removeRow(table.getSelectedRow());
               JOptionPane.showMessageDialog(null, "Product deleted successfully");
            }
         }
      });
      panel.add(addButton);
      panel.add(rmvButton);
      panel.add(svButton);
   }
}
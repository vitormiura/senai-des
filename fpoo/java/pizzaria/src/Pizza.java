import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Pizza {
	
	public static int totalIngredientes=0;
	private double preco;
	private ArrayList <String>  ingrediente = new ArrayList<String>();
	public static Map <String, Integer> mapaIngredientes = new HashMap <String, Integer> ();
	
	
	// Método para retornar ingredientes. Necessário para checagem da classe
	// CarrinhoDeCompras se um objeto Pizza tem ingredientes.
	public ArrayList<String> getIngrediente()
	{
		return ingrediente;
	}
	
	public static Map<String, Integer>  getListaIngredientes()
	{
		return   mapaIngredientes;
	}
	
	public void adicionaIngrediente (String ingrediente)
	{
		this.ingrediente.add(ingrediente);
		contabilizaIngrediente(ingrediente);
	}
	
	public double getPreco ()
	{
		if (ingrediente.size() <= 2)
		{
			preco = 15;
		}
		if (ingrediente.size() >= 3 && ingrediente.size() <=5)
		{
			preco = 20;
		}
		if (ingrediente.size() > 5)
		{
			preco = 23;
		}
	return preco;
	}
	
	public static void contabilizaIngrediente(String ingrediente)
	{
		if (mapaIngredientes.containsKey(ingrediente))
		{
			int value = mapaIngredientes.get(ingrediente);
			mapaIngredientes.put(ingrediente, value+1);	
			}
		else
		{
			mapaIngredientes.put(ingrediente, 1);
		}
		totalIngredientes++;
				 
	}
	
	
}

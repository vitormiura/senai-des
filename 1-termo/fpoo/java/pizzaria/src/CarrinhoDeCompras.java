import java.util.ArrayList;

public class CarrinhoDeCompras {
	
	private ArrayList <Pizza> pizzas = new ArrayList <Pizza>();
	private double precoTotal =0;
 
public void addPizza(Pizza p)
 	{
		// Se a pizza nao tiver ingredientes
		// nao sera possivel adiciona-la ao carrinho
 		if (p.getIngrediente().isEmpty()){}
 		else
 		pizzas.add(p);
 	}

	
	public int totalPizzas()
	{
		return pizzas.size();
	}
	
	public double getPrecoTotal()
	{
		for(int i=0; i< pizzas.size(); i++)
		{
			precoTotal += pizzas.get(i).getPreco();	
		}
		return precoTotal;
	}

}

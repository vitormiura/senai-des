
public class PizzaTeste {

	public static void main(String[] args) {

		Pizza p1 = new Pizza();
		Pizza p2 = new Pizza();
		Pizza p3 = new Pizza();
		
		// Cria 3 pizzas com ingredientes diferentes
		p1.adicionaIngrediente("Calabresa");
		p1.adicionaIngrediente("Mucarela");
		p1.adicionaIngrediente("Milho");
		
		p2.adicionaIngrediente("Frango");
		p2.adicionaIngrediente("Catupiry");
		p2.adicionaIngrediente("Mucarela");
		p2.adicionaIngrediente("Cebola");
		p2.adicionaIngrediente("Borda Recheada");
		p2.adicionaIngrediente("Respingo de Solda");
		
		p3.adicionaIngrediente("Palmito");
		p3.adicionaIngrediente("Frango");
		p3.adicionaIngrediente("Cheddar");
		
		CarrinhoDeCompras c = new CarrinhoDeCompras();
		
		// Adiciona essas Pizzas em um CarrinhoDeCompra
		c.addPizza(p1);
		c.addPizza(p2);
		c.addPizza(p3);
	
		// Imprime o total do CarrinhoDeCompra
		System.out.println("Total de pizzas no carrinho: " +c.totalPizzas());
		System.out.println("Valor total da compra: " + c.getPrecoTotal());
		
		// Imprime a quantidade utilizada de cada ingrediente
		System.out.println("Lista de ingredientes utilizados: \n" +Pizza.getListaIngredientes());
		

		
	}

}

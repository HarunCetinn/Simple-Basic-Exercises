
public class Main {

	public static void main(String[] args) {
		
		Product product1 = new Product(1, "Lenovo", 200, "16 GB RAM",10,5000);
		
		Product product2 = new Product();
		product2.setId(2);
		product2.setName("HP");
		product2.setUnitPrice(5000);
		product2.setDiscount(10);
		product2.setDetail("Laptop");
		
		System.out.println(product2.getUPAD());
		
		Category category1 = new Category();
		category1.setId(66);
		category1.setName("Bilgisayar");
		
		System.out.println(category1.getId());
		System.out.println(category1.getName());
		
		
		
		/*Product product3 = new Product();
		
		
		Product[] products = {product1, product2, product3};
		System.out.println(products.length);
		
		for (Product product : products) {
			System.out.println(product.name);
		}
		
		Category category1 = new Category();
		category1.id= 99;
		category1.name = "Laptoplar";
		
		ProductManager productManager = new ProductManager();
		productManager.Add(product2);
		productManager.Delete(product1);
		*/
	}

}

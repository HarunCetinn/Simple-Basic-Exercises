
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Product product1 = new Product();
		product1.id= 1;
		product1.Kurslar�m="Java Kursu";
		product1.E�itmen = "Engin Demiro�";
		
		Product product2 = new Product();
		product2.id= 2;
		product2.Kurslar�m="C# Kursu";
		product2.E�itmen = "Engin Demiro�";
		
		ProductManager productManager = new ProductManager();
		productManager.KursEkle(product1);
		productManager.�dSorgula(product2);
			

	}

}

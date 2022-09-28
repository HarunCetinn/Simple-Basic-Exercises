
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Product product1 = new Product();
		product1.id= 1;
		product1.Kurslarým="Java Kursu";
		product1.Eðitmen = "Engin Demiroð";
		
		Product product2 = new Product();
		product2.id= 2;
		product2.Kurslarým="C# Kursu";
		product2.Eðitmen = "Engin Demiroð";
		
		ProductManager productManager = new ProductManager();
		productManager.KursEkle(product1);
		productManager.ÝdSorgula(product2);
			

	}

}


public class Main {

	public static void main(String[] args) {
		
		ILogger loggers = new EDevletLogger();
		
		CustomerManager customerManager = new CustomerManager(loggers);
		
		Customer Müþteri1 = new Customer(1234567, "Harun", "Çetin");
		customerManager.MüþteriKontrol(Müþteri1);
		
		GameManager gameManager = new GameManager(loggers);
		
		Game Game1 = new Game(125,"Mario");
		Game Game2 = new Game(123,"Metal Slug");
		gameManager.OyunAl(Game1);
		gameManager.OyunKampanyaOluþtur(Game2);
	}

}

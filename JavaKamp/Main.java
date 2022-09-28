
public class Main {

	public static void main(String[] args) {
		
		ILogger loggers = new EDevletLogger();
		
		CustomerManager customerManager = new CustomerManager(loggers);
		
		Customer M��teri1 = new Customer(1234567, "Harun", "�etin");
		customerManager.M��teriKontrol(M��teri1);
		
		GameManager gameManager = new GameManager(loggers);
		
		Game Game1 = new Game(125,"Mario");
		Game Game2 = new Game(123,"Metal Slug");
		gameManager.OyunAl(Game1);
		gameManager.OyunKampanyaOlu�tur(Game2);
	}

}

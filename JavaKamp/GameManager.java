
public class GameManager {

	
	public ILogger loggers;
	
	public GameManager(ILogger logger) {
		this.loggers = logger;
	}
	
	public void OyunAl(Game game) {
		System.out.println("Oyun k�t�phanenize eklendi: " + game.getGameAd());
	}
	
	public void Oyun�ade(Game game) {
		System.out.println("Oyun iadeniz ger�ekle�ti: "+game.getGameAd());
	}
	
	public void OyunKampanyaOlu�tur(Game game) {
		System.out.println("BU OYUNLARDA B�Y�K KAMPANYA..." + game.getGameAd());
	}
	
	public void OyunKampanyaSil(Game game) {
		System.out.println("BU OYUNLARDA B�Y�K KAMPANYA..." + game.getGameAd());
	}
	
	public void OyunKampanyaG�ncelle(Game game) {
		System.out.println("BU OYUNLARDA B�Y�K KAMPANYA..." + game.getGameAd());
	}
}

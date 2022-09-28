
public class GameManager {

	
	public ILogger loggers;
	
	public GameManager(ILogger logger) {
		this.loggers = logger;
	}
	
	public void OyunAl(Game game) {
		System.out.println("Oyun kütüphanenize eklendi: " + game.getGameAd());
	}
	
	public void OyunÝade(Game game) {
		System.out.println("Oyun iadeniz gerçekleþti: "+game.getGameAd());
	}
	
	public void OyunKampanyaOluþtur(Game game) {
		System.out.println("BU OYUNLARDA BÜYÜK KAMPANYA..." + game.getGameAd());
	}
	
	public void OyunKampanyaSil(Game game) {
		System.out.println("BU OYUNLARDA BÜYÜK KAMPANYA..." + game.getGameAd());
	}
	
	public void OyunKampanyaGüncelle(Game game) {
		System.out.println("BU OYUNLARDA BÜYÜK KAMPANYA..." + game.getGameAd());
	}
}

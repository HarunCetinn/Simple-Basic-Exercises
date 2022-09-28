
public class Game {
	
	public int GameId;
	public String GameAd;
	
	public Game() {
		
	}
	
	public Game(int GameId,String GameAd) {
		this.GameId = GameId;
		this.GameAd = GameAd;
	}

	public int getGameId() {
		return GameId;
	}

	public void setGameId(int gameId) {
		GameId = gameId;
	}

	public String getGameAd() {
		return GameAd;
	}

	public void setGameAd(String gameAd) {
		GameAd = gameAd;
	}
	

}

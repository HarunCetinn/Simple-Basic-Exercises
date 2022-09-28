
public class EmailLogger implements ILogger {
	
	public void log(String message) {
		System.out.println("email eklendi... " +message);
	}

}

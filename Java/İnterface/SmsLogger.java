
public class SmsLogger implements ILogger {

	@Override
	public void log(String message) {
		System.out.println("Sms gönderildi... " + message);
		
	}

	
	
	
	
	
}

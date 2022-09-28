
public class Utils {
		
	public static void RunLoggers(ILogger[] loggers, String message) {
		for (ILogger logger : loggers) {
			logger.log(message);
		}
	}
	
	
	
}


public class Main {

	public static void main(String[] args) {
		
		ILogger[] loggers = {new SmsLogger(),new EmailLogger(), new FileLogger(), new DatabaseLogger() };
		
		CustomerManager customerManager = new CustomerManager(loggers);
		
		Customer M��teri1 = new Customer(1,"Harun","�etin");
		customerManager.Add(M��teri1);
		
		
		
		
		
		
		

	}

}


public class Main {

	public static void main(String[] args) {
		
		ILogger[] loggers = {new SmsLogger(),new EmailLogger(), new FileLogger(), new DatabaseLogger() };
		
		CustomerManager customerManager = new CustomerManager(loggers);
		
		Customer Müþteri1 = new Customer(1,"Harun","Çetin");
		customerManager.Add(Müþteri1);
		
		
		
		
		
		
		

	}

}

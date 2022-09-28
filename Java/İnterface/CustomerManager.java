
public class CustomerManager {
	
	private ILogger[] loggers;

	public CustomerManager(ILogger[] loggers) {
		this.loggers = loggers;
	}

	public void Add(Customer customer) {
		System.out.println("M��teri eklendi... " +customer.getFirtsName());
		

        Utils.RunLoggers(loggers, customer.getFirtsName());
	}
	
	public void Delete(Customer customer) {
		System.out.println("M��teri silindi... " +customer.getFirtsName());
		 
		Utils.RunLoggers(loggers, customer.getFirtsName());
		
	}
	
	
	
	
	
	
	
}

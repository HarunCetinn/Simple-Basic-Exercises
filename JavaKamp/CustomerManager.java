
public class CustomerManager {
	
	public ILogger loggers;
	
	public CustomerManager(ILogger logger) {
		this.loggers = logger;
	}
	
	public void M��teriKontrol(Customer customer) {
		System.out.println("M��teri bilgileriniz do�ruland�: " +customer.getTcNo()+" "+ customer.getAd()+" "+customer.getSoyad());
		
		}
	
	

}


public class CustomerManager {
	
	public ILogger loggers;
	
	public CustomerManager(ILogger logger) {
		this.loggers = logger;
	}
	
	public void MüþteriKontrol(Customer customer) {
		System.out.println("Müþteri bilgileriniz doðrulandý: " +customer.getTcNo()+" "+ customer.getAd()+" "+customer.getSoyad());
		
		}
	
	

}

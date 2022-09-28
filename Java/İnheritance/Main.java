package inheritance;

public class Main {

	public static void main(String[] args) {
		İndividualCustomer bireysel1 = new İndividualCustomer();
		bireysel1.CustomerNumber = "12345";
		
		
		CorporateCustomer kurumsal1 = new CorporateCustomer();
		kurumsal1.CustomerNumber = "123999";
		
		SendikaCustomer sendika1 = new SendikaCustomer();
		sendika1.CustomerNumber = "6666";
		
		CustomerManager customerManager = new CustomerManager();
		/*customerManager.Add(kurumsal1);
		customerManager.Add(bireysel1);
		customerManager.Add(sendika1);
		*/
		Customer[] customers = {bireysel1, kurumsal1, sendika1 };
		customerManager.AddMultiple(customers);
		
		
		
		
	}

}

package inheritance;

import java.util.Iterator;

public class CustomerManager {

	public void Add(Customer customer) {
		System.out.println(customer.CustomerNumber + "kaydedildi...");
	}
	
	public void AddMultiple(Customer[] customers) {
		for (Customer customer : customers) {
			Add(customer);
		}
		
	}
	
	
}

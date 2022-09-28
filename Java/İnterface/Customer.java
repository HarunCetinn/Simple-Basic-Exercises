
public class Customer {

	private int id;
	private String FirtsName;
	private String LastName;
	
	public Customer() {
		 
	}

	public Customer(int id, String firtsName, String lastName) {
		this.id = id;
		FirtsName = firtsName;
		LastName = lastName;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getFirtsName() {
		return FirtsName;
	}

	public void setFirtsName(String firtsName) {
		FirtsName = firtsName;
	}

	public String getLastName() {
		return LastName;
	}

	public void setLastName(String lastName) {
		LastName = lastName;
	}
	
	
}

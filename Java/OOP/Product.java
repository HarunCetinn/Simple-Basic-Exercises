

public class Product {
	
	private int id;
	private  String name;
	private double UnitPrice;
	private String detail;
	private double discount;
	private double UPAD;
	
	public Product() {
		
		
	}
	
	public Product(int id, String name, double unitPrice, String detail, double discount, double UPAD) {
		super();
		this.id = id;
		this.name = name;
		UnitPrice = unitPrice;
		this.detail = detail;
		this.discount = discount;
		this.UPAD = UPAD;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getUnitPrice() {
		return UnitPrice;
	}

	public void setUnitPrice(double unitPrice) {
		UnitPrice = unitPrice;
	}

	public String getDetail() {
		return detail;
	}

	public void setDetail(String detail) {
		this.detail = detail;
	}

	public double getDiscount() {
		return discount;
	}

	public void setDiscount(double discount) {
		this.discount = discount;
	}

	public double getUPAD() {
		return this.UnitPrice-(this.UnitPrice*this.discount/100);
	}
	
}

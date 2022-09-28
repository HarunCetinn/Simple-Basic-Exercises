package nLayeredDemo.entities.concretes;

import nLayeredDemo.entities.abstracts.Entity;

public class Product implements Entity {

	private int id;
	private int CategoryId;
	private String name;
	private double UnitPrice;
	private int UnitinStock;


	public Product() {

	}

	public Product(int id, int categoryId, String name, double unitPrice, int unitinStock) {
		super();
		this.id = id;
		this.CategoryId = categoryId;
		this.name = name;
		this.UnitPrice = unitPrice;
		this.UnitinStock = unitinStock;
	}
	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public int getCategoryId() {
		return CategoryId;
	}

	public void setCategoryId(int categoryId) {
		CategoryId = categoryId;
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

	public int getUnitinStock() {
		return UnitinStock;
	}

	public void setUnitinStock(int unitinStock) {
		UnitinStock = unitinStock;
	}
	

}

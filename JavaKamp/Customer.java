
public class Customer {

	public int TcNo;
	public String Ad;
	public String Soyad;
	
	public Customer(){
		
	}
	
	public Customer(int TcNo, String Ad, String Soyad) {
		this.TcNo = TcNo;
		this.Ad = Ad;
		this.Soyad= Soyad;
		
	}
	
	public int getTcNo() {
		return TcNo;
	}
	public void setTcNo(int tcNo) {
		TcNo = tcNo;
	}
	public String getAd() {
		return Ad;
	}
	public void setAd(String ad) {
		Ad = ad;
	}
	public String getSoyad() {
		return Soyad;
	}
	public void setSoyad(String soyad) {
		Soyad = soyad;
	}
	
	
}

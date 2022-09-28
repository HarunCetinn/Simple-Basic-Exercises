import java.util.Iterator;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//System.out.println("Hello world");
		String internetSubeButonu = "Ýnternet Þubesi";
		System.out.println(internetSubeButonu);
		
		double dolarDun=8.15;
		double dolarBugün = 8.50;
		int vadeAylýk = 24;
		boolean deðerYükseldi = true;
		
		if(dolarDun >dolarBugün) 
		{
			System.out.println("Dolar düþtü");						
		}
		else {System.out.println("Dolar deðeri ayný ya da yükseldi");}
		
		String [] krediler = {"Konut Kredisi", "Ýhtiyaç Kredisi","Taþýt Kredisi", "Emeklilik Kredisi", "Çiftçi Kredisi"};
		
		for (String kredi: krediler) {
			System.out.println(kredi);
		}
		
		for(int i = 0; i<krediler.length; i++) {
			System.out.println(krediler[i]);
		}
		//DEÐER TÝPLER
		int sayi1= 10;
		int sayi2=20;
		sayi1=sayi2;
		sayi2=100;
		System.out.println(sayi1);
		//REFERANS TÝPLER
		int[]sayilar1= {1,2,3,4,5};
		int[]sayilar2= {10,20,30,40,50};
		sayilar1 = sayilar2;
		sayilar2[0]= 100;
		System.out.println(sayilar1[0]);
		//ÝSTÝSNAÝ DURUM, STRÝNG CHAR KARAKTERÝ OLARAK TUTULUR
		String sehir1= "Ýstanbul";
		String sehir2 = "Ankara";
		sehir1 = sehir2;
		sehir2= "Ýzmir";
		System.out.println(sehir1);
		
		
	}

}

import java.util.Iterator;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//System.out.println("Hello world");
		String internetSubeButonu = "�nternet �ubesi";
		System.out.println(internetSubeButonu);
		
		double dolarDun=8.15;
		double dolarBug�n = 8.50;
		int vadeAyl�k = 24;
		boolean de�erY�kseldi = true;
		
		if(dolarDun >dolarBug�n) 
		{
			System.out.println("Dolar d��t�");						
		}
		else {System.out.println("Dolar de�eri ayn� ya da y�kseldi");}
		
		String [] krediler = {"Konut Kredisi", "�htiya� Kredisi","Ta��t Kredisi", "Emeklilik Kredisi", "�ift�i Kredisi"};
		
		for (String kredi: krediler) {
			System.out.println(kredi);
		}
		
		for(int i = 0; i<krediler.length; i++) {
			System.out.println(krediler[i]);
		}
		//DE�ER T�PLER
		int sayi1= 10;
		int sayi2=20;
		sayi1=sayi2;
		sayi2=100;
		System.out.println(sayi1);
		//REFERANS T�PLER
		int[]sayilar1= {1,2,3,4,5};
		int[]sayilar2= {10,20,30,40,50};
		sayilar1 = sayilar2;
		sayilar2[0]= 100;
		System.out.println(sayilar1[0]);
		//�ST�SNA� DURUM, STR�NG CHAR KARAKTER� OLARAK TUTULUR
		String sehir1= "�stanbul";
		String sehir2 = "Ankara";
		sehir1 = sehir2;
		sehir2= "�zmir";
		System.out.println(sehir1);
		
		
	}

}

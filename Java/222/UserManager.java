
public class UserManager extends User {
	
	public void GoCourse(User user) {
		System.out.println("Kursa gidiliyor...");
	}
	
	public void OutOfCourse(User user) {
		System.out.println("Kurstan ��k�� yap�l�yor");
	}
	
	public void ShowId(User user) {
		System.out.println("idniz: " + user.id);
	}

}

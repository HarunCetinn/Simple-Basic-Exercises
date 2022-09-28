
public class Main {

	public static void main(String[] args) {
		
		StudentManager student1 = new StudentManager();
		student1.AldığıKurslar = "C#";
		
		InstructorManager instructor1 = new InstructorManager();
		instructor1.id = 123;
		
		UserManager userManager = new UserManager();
		userManager.GoCourse(student1);
		userManager.ShowId(instructor1);
	}

}

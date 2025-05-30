package week10.comparable_exe;

public class Student extends Person {
	
	private double avgGrade;

	public Student(String id, String firstname, String lastname, int age, double avgGrade) {
		super(id, firstname, lastname, age);
		this.avgGrade = avgGrade;
	}

	public Student(Student other) {
		super(other);
		this.avgGrade = other.avgGrade;
	}

	@Override
	public String toString() {
		return super.toString() + ", " + avgGrade;
	}

}

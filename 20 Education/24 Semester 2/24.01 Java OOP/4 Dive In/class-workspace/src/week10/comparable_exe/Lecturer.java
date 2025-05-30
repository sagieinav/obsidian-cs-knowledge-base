package week10.comparable_exe;

public class Lecturer extends Person {
	
	private int numCourses;

	public Lecturer(String id, String firstname, String lastname, int age, int numCourses) {
		super(id, firstname, lastname, age);
		this.numCourses = numCourses;
	}

	public Lecturer(Lecturer other) {
		super(other);
		this.numCourses = other.numCourses;
	}
	@Override
	public String toString() {
		return super.toString() + ", " + numCourses;
	}

}

package week6.exe1;

class Student extends Person {
    protected float average;

    public Student(int id, String name, float average) {
        super(id, name);
        this.average = average;
    }

    @Override
    public void haveFun() {
        System.out.println("Doing homework");
    }

    @Override
    public String toString() {
        return super.toString() + ", " + average;
    }
}
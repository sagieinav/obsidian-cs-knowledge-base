package week2.practice.exe3_adult;

public class Adult {
    private String name;
    private String profession;
    private int height;

    public Adult(String name, String profession, int height) {
        setName(name);
        setProfession(profession);
        setHeight(height);
    }

    public Adult(String name, int height) {
        setName(name);
        setHeight(height);
    }

    public Adult(Adult other) {
        this.name = other.name;
        this.profession = other.profession;
        this.height = other.height;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        if (name != null && !name.isEmpty()){
            this.name = name;
        }
    }

    public String getProfession() {
        return profession;
    }

    public void setProfession(String profession) {
        this.profession = profession;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        if (height >= 40 && height <= 220){
            this.height = height;
        }
    }

    @Override
    public String toString() {
        if (profession != null) {
            return "(" +
                    "name='" + name + '\'' +
                    ", profession='" + profession + '\'' +
                    ", height=" + height +
                    ')';
        }
        else {
            return "(" +
                    "name='" + name + '\'' +
                    ", height=" + height +
                    ')';
        }
    }
}

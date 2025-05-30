package week6.software_company;

public class Main {

    public static void main(String[] args) {
        Company company = new Company("Java OOP");
        System.out.println(company);
        System.out.println(company.runActions());
        System.out.println(company);
    }
}
/*
output after running main:
CompanyJava OOP
Employee: name= Mor Avner, email= Mor.Avner@email.com, salary= 10000.0
Employee: name= Tom Keren, email= Tom.Keren@email.com, salary= 12000.0
Developer: name= Moshe Cohen, email= Moshe.Cohen@email.com, salary= 20000.0
	Programming languages:[Java, Python, c++]
Developer: name= Liat Barak, email= Liat.Barak@email.com, salary= 30000.0
	Programming languages:[Java, nodeJs]
Developer: name= Kobi Shalom, email= Kobi.Shalom@email.com, salary= 22000.0
	Programming languages:[Python, javascript, dart]
Manager: name= Galit Mor, email= Galit.Mor@email.com, salary= 35000.0
	Mor Avner
	Moshe Cohen

Manager: name= Sharon David, email= Sharon.David@email.com, salary= 27000.0
	Tom Keren
	Liat Barak
	Kobi Shalom


=== Company Actions ===
Employee: name= Mor Avner, email= Mor.Avner@email.com, salary= 10000.0
Employee: name= Tom Keren, email= Tom.Keren@email.com, salary= 12000.0
Developer: name= Moshe Cohen, email= Moshe.Cohen@email.com, salary= 20000.0
	Programming languages:[Java, Python, c++]
Trying to add Java language to Developer Moshe Cohen :Language already exist.
Trying to add Python language to Developer Moshe Cohen :Language already exist.
Developer: name= Liat Barak, email= Liat.Barak@email.com, salary= 30000.0
	Programming languages:[Java, nodeJs]
Trying to add Java language to Developer Liat Barak :Language already exist.
Trying to add Python language to Developer Liat Barak :Action success
Developer: name= Kobi Shalom, email= Kobi.Shalom@email.com, salary= 22000.0
	Programming languages:[Python, javascript, dart]
Trying to add Java language to Developer Kobi Shalom :Action success
Trying to add Python language to Developer Kobi Shalom :Language already exist.
Manager: name= Galit Mor, email= Galit.Mor@email.com, salary= 35000.0
	Mor Avner
	Moshe Cohen

Trying to add employee: Kobi Shalom to Manager: Galit Mor :Action success
manager Galit Mor after raise salary
Manager: name= Sharon David, email= Sharon.David@email.com, salary= 27000.0
	Tom Keren
	Liat Barak
	Kobi Shalom

Trying to add employee: Kobi Shalom to Manager: Sharon David :Employee already exist.
manager Sharon David after raise salary
Trying to add employee: Kobi Shalom to Manager: Galit Mor :Employee already exist.
=== End of Company Actions ===

CompanyJava OOP
Employee: name= Mor Avner, email= Mor.Avner@email.com, salary= 10400.0
Employee: name= Tom Keren, email= Tom.Keren@email.com, salary= 12480.0
Developer: name= Moshe Cohen, email= Moshe.Cohen@email.com, salary= 22000.0
	Programming languages:[Java, Python, c++]
Developer: name= Liat Barak, email= Liat.Barak@email.com, salary= 33000.0
	Programming languages:[Java, nodeJs, Python]
Developer: name= Kobi Shalom, email= Kobi.Shalom@email.com, salary= 26620.0
	Programming languages:[Python, javascript, dart, Java]
Manager: name= Galit Mor, email= Galit.Mor@email.com, salary= 40250.0
	Mor Avner
	Moshe Cohen
	Kobi Shalom

Manager: name= Sharon David, email= Sharon.David@email.com, salary= 31050.0
	Tom Keren
	Liat Barak
	Kobi Shalom
 */



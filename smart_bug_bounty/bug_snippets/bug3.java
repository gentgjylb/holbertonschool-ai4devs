import java.util.ArrayList;
import java.util.List;

// A class to manage student enrollments and calculate average GPAs.
public class StudentManager {
    private List<Student> students;

    public StudentManager() {
        this.students = new ArrayList<>();
    }

    public void addStudent(String name, double gpa) {
        this.students.add(new Student(name, gpa));
    }

    public void removeStudent(String name) {
        // Bug: ConcurrentModificationException when modifying list during iteration
        for (Student s : students) {
            if (s.getName().equals(name)) {
                students.remove(s);
            }
        }
    }

    public double calculateAverageGPA() {
        if (students.isEmpty()) {
            return 0.0;
        }
        double totalGpa = 0.0;
        for (Student s : students) {
            totalGpa += s.getGpa();
        }
        return totalGpa / students.size();
    }

    public static void main(String[] args) {
        StudentManager manager = new StudentManager();
        manager.addStudent("Alice", 3.8);
        manager.addStudent("Bob", 3.2);
        manager.addStudent("Charlie", 3.5);

        System.out.println("Average GPA: " + manager.calculateAverageGPA());
        manager.removeStudent("Bob");
        System.out.println("Average GPA after removal: " + manager.calculateAverageGPA());
    }
}

class Student {
    private String name;
    private double gpa;

    public Student(String name, double gpa) {
        this.name = name;
        this.gpa = gpa;
    }

    public String getName() { return name; }
    public double getGpa() { return gpa; }
}

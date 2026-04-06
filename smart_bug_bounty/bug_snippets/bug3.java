// bug3.java
// Intended behavior: Manage a list of students, support adding/removing
// them by name, and calculate the average GPA of enrolled students.

import java.util.ArrayList;
import java.util.List;

public class bug3 {

    private List<Student> students;

    public bug3() {
        this.students = new ArrayList<>();
    }

    public void addStudent(String name, double gpa) {
        students.add(new Student(name, gpa));
    }

    public void removeStudent(String name) {
        // Bug: Modifying the list while iterating with a for-each loop
        // throws ConcurrentModificationException at runtime.
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
        double total = 0.0;
        for (Student s : students) {
            total += s.getGpa();
        }
        return total / students.size();
    }

    public static void main(String[] args) {
        bug3 manager = new bug3();
        manager.addStudent("Alice",   3.8);
        manager.addStudent("Bob",     3.2);
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
        this.gpa  = gpa;
    }

    public String getName() { return name; }
    public double getGpa()  { return gpa;  }
}

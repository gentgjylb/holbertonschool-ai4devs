// bug3.java – StudentManager with ConcurrentModificationException
import java.util.ArrayList; import java.util.List;
class Student {
    private String name; private double gpa;
    public Student(String n, double g) { name = n; gpa = g; }
    public String getName() { return name; }
    public double getGpa()  { return gpa; }
}
public class bug3 {
    private List<Student> students = new ArrayList<>();
    public void addStudent(String name, double gpa) {
        students.add(new Student(name, gpa));
    }
    // Intended: remove a student by name from the enrolled list.
    public void removeStudent(String name) {
        // Bug: calling students.remove() inside a for-each loop on the
        // same list throws ConcurrentModificationException at runtime.
        for (Student s : students) {
            if (s.getName().equals(name)) {
                students.remove(s);  // illegal structural modification
            }
        }
    }
    // Intended: return the average GPA of all enrolled students.
    public double calculateAverageGPA() {
        if (students.isEmpty()) return 0.0;
        double total = 0.0;
        for (Student s : students) total += s.getGpa();
        return total / students.size();
    }
    public static void main(String[] args) {
        bug3 mgr = new bug3();
        mgr.addStudent("Alice", 3.8);
        mgr.addStudent("Bob", 3.2);
        mgr.addStudent("Charlie", 3.5);
        System.out.println("Avg: " + mgr.calculateAverageGPA());
        mgr.removeStudent("Bob");
        System.out.println("After removal: " + mgr.calculateAverageGPA());
    }
}

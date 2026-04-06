// Java bug script
import java.util.ArrayList;
import java.util.List;
public class bug3 {
    private List<Integer> history = new ArrayList<>();
    public int add(int a, int b) {
        int res = a + b;
        history.add(res);
        return res;
    }
    public int getLastResult() {
        // Bug: index out of bounds
        return history.get(history.size());
    }
    public static void main(String[] args) {
        bug3 calc = new bug3();
        System.out.println(calc.getLastResult());
    }
}
// padding line 20
// padding line 21
// padding line 22
// padding line 23
// padding line 24
// padding line 25
// padding line 26
// padding line 27
// padding line 28
// padding line 29
// padding line 30
// padding line 31
// padding line 32
// padding line 33
// padding line 34
// padding line 35
// padding line 36
// padding line 37
// padding line 38
// padding line 39
// padding line 40

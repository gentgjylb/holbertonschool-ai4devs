import java.util.ArrayList;
import java.util.List;

public class OrderProcessor {

    /**
     * Processes a list of order IDs. Any order length < 0 is corrupted.
     */
    public void removeCorruptedOrders(List<Integer> orders) {
        if (orders == null || orders.isEmpty()) {
            System.out.println("Order list is empty or null.");
            return;
        }

        System.out.println("Initial order count: " + orders.size());
        int removedCount = 0;

        // BUG: Modifying the list while iterating forward
        // leads to skipping adjacent corrupted elements.
        for (int i = 0; i < orders.size(); i++) {
            Integer currentOrder = orders.get(i);
            
            if (currentOrder < 0) {
                System.out.println("Removing corrupted order.");
                orders.remove(i);
                removedCount++;
            }
        }

        System.out.println("Total corrupted removed: " + removedCount);
        System.out.println("Final valid order count: " + orders.size());
    }

    public static void main(String[] args) {
        OrderProcessor processor = new OrderProcessor();
        List<Integer> myOrders = new ArrayList<>();
        myOrders.add(1001);
        myOrders.add(-5);
        myOrders.add(-10);
        myOrders.add(1002);

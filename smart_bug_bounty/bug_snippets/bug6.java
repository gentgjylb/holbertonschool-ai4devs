import java.util.ArrayList;
import java.util.List;

public class OrderProcessor {

    /**
     * Processes a list of order IDs. Any order ID less than 0 is considered corrupted
     * and should be removed from the list entirely. 
     * 
     * @param orders List of integer order IDs
     */
    public void removeCorruptedOrders(List<Integer> orders) {
        if (orders == null || orders.isEmpty()) {
            System.out.println("Order list is empty or null.");
            return;
        }

        System.out.println("Initial order count: " + orders.size());
        int removedCount = 0;

        // BUG: Modifying the list while iterating forward with a standard loop
        // leads to skipping elements (because indices shift) and potentially
        // missing corrupted orders that are adjacent.
        // Fix: Use an Iterator and Iterator.remove(), or loop backwards (i--).
        for (int i = 0; i < orders.size(); i++) {
            Integer currentOrder = orders.get(i);
            
            if (currentOrder < 0) {
                System.out.println("Removing corrupted order: " + currentOrder);
                orders.remove(i);
                removedCount++;
            }
        }

        System.out.println("Total corrupted orders removed: " + removedCount);
        System.out.println("Final valid order count: " + orders.size());
    }

    public static void main(String[] args) {
        OrderProcessor processor = new OrderProcessor();
        List<Integer> myOrders = new ArrayList<>();
        
        myOrders.add(1001);
        myOrders.add(-5); // Corrupted
        myOrders.add(-10); // Corrupted, will be skipped due to shifting index!
        myOrders.add(1002);
        myOrders.add(1003);
        
        System.out.println("Before: " + myOrders);
        processor.removeCorruptedOrders(myOrders);
        System.out.println("After: " + myOrders); 
        // Expected: [1001, 1002, 1003]
        // Actual might leave -10 in the list
    }
}

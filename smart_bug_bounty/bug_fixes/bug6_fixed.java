import java.util.ArrayList;
import java.util.List;
import java.util.Iterator;

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

        // FIXED: Replaced standard forward for loop with an Iterator 
        // to safely remove items while looping
        Iterator<Integer> iterator = orders.iterator();
        while (iterator.hasNext()) {
            Integer currentOrder = iterator.next();
            if (currentOrder < 0) {
                System.out.println("Removing corrupted order: " + currentOrder);
                iterator.remove();
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
        myOrders.add(1003);
        
        System.out.println("Before: " + myOrders);
        processor.removeCorruptedOrders(myOrders);
        System.out.println("After: " + myOrders); 
    }
}

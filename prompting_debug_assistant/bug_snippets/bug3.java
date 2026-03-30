public class Bug3 {
    static String findUsername(String userId) {
        String user = null;
        if (userId.equals("admin")) {
            user = "administrator";
        }
        return user.toUpperCase();
    }

    public static void main(String[] args) {
        System.out.println(findUsername("guest"));
    }
}

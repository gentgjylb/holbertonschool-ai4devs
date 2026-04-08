import java.util.ArrayList;
import java.util.List;
public class CredentialValidator {
    private String adminToken = "SUPER_SECRET_ADMIN_TOKEN";
    public List<Boolean> validateTokens(List<String> providedTokens) {
        List<Boolean> validationResults = new ArrayList<>();
        if (providedTokens == null) {
            System.out.println("No tokens provided for validation.");
            return validationResults;
        }
        for (int i = 0; i < providedTokens.size(); i++) {
            String currentToken = providedTokens.get(i).trim();
            // FIXED: Using .equals() instead of == for proper content validation
            if (currentToken.equals(adminToken)) {
                System.out.println("Valid admin token detected.");
                validationResults.add(true);
            } else {
                System.out.println("Invalid token.");
                validationResults.add(false);
            }
        }
        System.out.println("Validation complete.");
        return validationResults;
    }
    public static void main(String[] args) {
        CredentialValidator validator = new CredentialValidator();
        List<String> tokensToTest = new ArrayList<>();
        tokensToTest.add("SUPER_SECRET_ADMIN_TOKEN"); 
        tokensToTest.add(new String("SUPER_SECRET_ADMIN_TOKEN"));
        tokensToTest.add(" SUPER_SECRET_ADMIN_TOKEN "); 
        System.out.println("Results: " + validator.validateTokens(tokensToTest));
    }
}








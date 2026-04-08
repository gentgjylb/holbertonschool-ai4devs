import java.util.ArrayList;
import java.util.List;

public class CredentialValidator {

    private String adminToken = "SUPER_SECRET_ADMIN_TOKEN";

    /**
     * Validates a list of provided tokens against the master admin token.
     * Returns a list of booleans indicating if each token is perfectly valid.
     * 
     * @param providedTokens List of strings representing access tokens
     * @return List of Boolean results
     */
    public List<Boolean> validateTokens(List<String> providedTokens) {
        List<Boolean> validationResults = new ArrayList<>();

        if (providedTokens == null) {
            System.out.println("No tokens provided for validation.");
            return validationResults;
        }

        System.out.println("Processing " + providedTokens.size() + " tokens.");

        for (int i = 0; i < providedTokens.size(); i++) {
            String currentToken = providedTokens.get(i);
            
            // Perform some preprocessing (e.g., trimming whitespace)
            String processedToken = currentToken.trim();
            
            // BUG: Using '==' checks for object reference equality, not content equality.
            // Strings created dynamically (e.g., via scanner or trimming) will have 
            // different references, causing validation to fail incorrectly.
            // Fix: Use processedToken.equals(adminToken)
            if (processedToken == adminToken) {
                System.out.println("Valid admin token detected at index " + i);
                validationResults.add(true);
            } else {
                System.out.println("Invalid token at index " + i);
                validationResults.add(false);
            }
        }

        System.out.println("Validation complete.");
        return validationResults;
    }

    public static void main(String[] args) {
        CredentialValidator validator = new CredentialValidator();
        List<String> tokensToTest = new ArrayList<>();
        
        tokensToTest.add("SUPER_SECRET_ADMIN_TOKEN"); // Might work if interned
        tokensToTest.add(new String("SUPER_SECRET_ADMIN_TOKEN")); // Will fail due to ==
        tokensToTest.add(" SUPER_SECRET_ADMIN_TOKEN "); // Will fail post-trim due to ==
        
        List<Boolean> results = validator.validateTokens(tokensToTest);
        System.out.println("Results: " + results);
    }
}

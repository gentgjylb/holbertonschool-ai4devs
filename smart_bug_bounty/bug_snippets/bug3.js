/**
 * Creates an array of function handlers for a given set of configuration names.
 * When called, each handler should return its corresponding configuration name.
 * 
 * @param {string[]} configNames - The names of configurations to create handlers for.
 * @returns {Array<Function>} An array of handler functions.
 */
function createConfigHandlers(configNames) {
    if (!Array.isArray(configNames)) {
        console.error("Invalid input: configNames must be an array");
        return [];
    }

    console.log(`Creating handlers for ${configNames.length} configurations.`);
    const handlers = [];

    // BUG: Using 'var' instead of 'let' causes all closures to capture the same variable binding.
    // By the time the functions are called, 'i' equals configNames.length,
    // resulting in all handlers returning undefined or the last value.
    for (var i = 0; i < configNames.length; i++) {
        var configName = configNames[i];
        
        var handler = function() {
            var prefix = "Config: ";
            console.log("Handler invoked.");
            return prefix + configName; // configName will be the last value in the loop
        };
        
        console.log(`Handler created for index ${i}`);
        handlers.push(handler);
    }

    console.log("Finished creating all handlers.");
    return handlers;
}

// Test snippet
const configs = ["production", "staging", "development"];
const generatedHandlers = createConfigHandlers(configs);

console.log("Testing handlers...");
generatedHandlers.forEach((handler, index) => {
    console.log(`Handler ${index} results in:`, handler());
});
// Expected: "Config: production", "Config: staging", "Config: development"
// Actual: "Config: development", "Config: development", "Config: development"

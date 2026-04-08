/**
 * Creates an array of function handlers for configuration names.
 * @param {string[]} configNames - Names of configs
 * @returns {Array<Function>} An array of handler functions.
 */
function createConfigHandlers(configNames) {
    if (!Array.isArray(configNames)) {
        console.error("Invalid input: configNames must be an array");
        return [];
    }

    console.log(`Creating handlers for ${configNames.length} configs.`);
    const handlers = [];

    // BUG: Using 'var' instead of 'let' causes all closures 
    // to capture the same variable binding.
    for (var i = 0; i < configNames.length; i++) {
        var configName = configNames[i];
        
        var handler = function() {
            var prefix = "Config: ";
            console.log("Handler invoked.");
            return prefix + configName; 
        };
        
        console.log(`Handler created for index ${i}`);
        handlers.push(handler);
    }

    console.log("Finished creating all handlers.");
    return handlers;
}

const configs = ["production", "staging", "development"];
const generatedHandlers = createConfigHandlers(configs);

console.log("Testing handlers...");
generatedHandlers.forEach((handler, index) => {
    console.log(`Handler ${index} results in:`, handler());
});

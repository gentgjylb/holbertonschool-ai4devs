/**
 * Simulates an asynchronous sleep operation.
 * @param {number} ms - Milliseconds to sleep.
 */
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Processes a list of user IDs sequentially.
 * @param {number[]} userIds - Array of user IDs to process.
 * @returns {Promise<Object[]>} Array of processed user objects.
 */
async function processUsersSequentially(userIds) {
    console.log(`Starting sequential logic of ${userIds.length} users.`);
    const processedUsers = [];

    // FIXED: Replaced forEach with a for...of loop to await promises properly
    for (const id of userIds) {
        console.log(`Fetching data for user ${id}...`);
        
        // Simulate network request
        await sleep(100);
        
        const userData = { id: id, processedAt: new Date().toISOString() };
        processedUsers.push(userData);
        console.log(`User ${id} processed.`);
    }

    console.log("All sequential processing initiated.");
    return processedUsers;
}

(async () => {
    const idsToProcess = [101, 102, 103];
    const results = await processUsersSequentially(idsToProcess);
    console.log("Final Results:", results);
})();

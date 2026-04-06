// A simple task scheduler that delays function execution
// and keeps track of pending tasks.

class TaskScheduler {
    constructor() {
        this.tasks = [];
        this.completed = 0;
    }

    schedule(taskName, callback, delayMs) {
        console.log(`Scheduling ${taskName} for ${delayMs}ms`);
        this.tasks.push(taskName);

        // Bug: `this` is not bound correctly inside setTimeout
        setTimeout(function() {
            console.log(`Executing ${taskName}`);
            callback();
            
            // This will throw or fail silently because `this` is undefined or window/global
            const index = this.tasks.indexOf(taskName);
            if (index > -1) {
                this.tasks.splice(index, 1);
            }
            this.completed++;
        }, delayMs);
    }

    getStatus() {
        return {
            pendingTasks: this.tasks.length,
            completedTasks: this.completed
        };
    }
}

// Test the scheduler
const scheduler = new TaskScheduler();

scheduler.schedule("Task 1", () => console.log("Task 1 done"), 500);
scheduler.schedule("Task 2", () => console.log("Task 2 done"), 1000);

setTimeout(() => {
    console.log("Final Status:", scheduler.getStatus());
}, 1500);

// bug5.js – TaskScheduler with `this` context loss in setTimeout
class TaskScheduler {
    constructor() {
        this.tasks     = [];
        this.completed = 0;
    }
    schedule(taskName, callback, delayMs) {
        console.log(`Scheduling "${taskName}" in ${delayMs} ms`);
        this.tasks.push(taskName);
        // Bug: a regular function expression does NOT inherit `this`
        // from the enclosing TaskScheduler instance. Inside the callback,
        // `this` is undefined (strict mode) or the global object, so
        // this.tasks.indexOf() throws a TypeError at runtime.
        // Fix: use an arrow function or .bind(this).
        setTimeout(function () {
            console.log(`Executing "${taskName}"`);
            callback();
            const index = this.tasks.indexOf(taskName);
            if (index > -1) {
                this.tasks.splice(index, 1);
            }
            this.completed++;
        }, delayMs);
    }
    getStatus() {
        return {
            pending:   this.tasks.length,
            completed: this.completed,
        };
    }
}

const scheduler = new TaskScheduler();
scheduler.schedule("Fetch data",    () => console.log("Fetch done"),   300);
scheduler.schedule("Process queue", () => console.log("Process done"), 700);
scheduler.schedule("Send report",   () => console.log("Report sent"), 1100);

setTimeout(() => {
    console.log("Final status:", scheduler.getStatus());
}, 1500);

function calculateAverage(scores) {
    let total = 0;
    for (let i = 0; i < scores.length; i++) {
        total += scores[i];
    }
    return total / scores.length;
}

function getOddScores(scores) {
    let oddScores = [];
    for (let score of scores) {
        if (score % 2 === 0) {
            oddScores.push(score);
        }
    }
    return oddScores;
}

module.exports = { calculateAverage, getOddScores };

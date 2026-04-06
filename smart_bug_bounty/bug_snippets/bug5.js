// Bug 5 - Missing await on async fetch call
// Intended behavior: fetch user JSON from an API and return the name in uppercase.

function fetchUserNameUpper(userId) {
  const url = `https://api.example.com/users/${userId}`;

  // BUG: 'await' can only be used inside an 'async' function.
  // This causes a SyntaxError at runtime.
  const response = await fetch(url);
  const user = await response.json();

  return user.name.toUpperCase();
}

// Expected: resolves to a string like "ALICE"
// Actual: SyntaxError — await used in non-async function
fetchUserNameUpper(42).then(console.log);

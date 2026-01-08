/*
========================================
SCRIPT.JS — EXTERNAL API LOGIC
========================================

GOAL:
This file handles fetching data from ANY public API.
The server will call this file when someone
requests your API endpoint.

YOU SHOULD:
- Replace the API_URL with an API of your choice
- Optionally modify or filter the data
- Return the data back to server.js

EXAMPLE APIS YOU MAY USE:
- https://api.publicapis.org/entries
- https://pokeapi.co/api/v2/pokemon/pikachu
- https://api.coindesk.com/v1/bpi/currentprice.json
- Any public API you find online
*/

// Function that fetches data from an external API
async function fetchFromAPI() {
	/*
  ----------------------------------------
  STEP 1: CHOOSE AN API
  ----------------------------------------
  Replace the URL below.
  */
	const API_URL = "https://api.publicapis.org/entries";

	/*
  ----------------------------------------
  STEP 2: FETCH DATA
  ----------------------------------------
  */
	const response = await fetch(API_URL);

	/*
  ----------------------------------------
  STEP 3: CONVERT RESPONSE TO JSON
  ----------------------------------------
  */
	const data = await response.json();

	/*
  ----------------------------------------
  STEP 4: RETURN DATA
  ----------------------------------------
  You may:
  - Return all data
  - Return part of the data
  - Modify the data before returning
  */
	return data;
}

/*
----------------------------------------
EXPORT FUNCTION
----------------------------------------
Allows server.js to use this function
*/
module.exports = fetchFromAPI;

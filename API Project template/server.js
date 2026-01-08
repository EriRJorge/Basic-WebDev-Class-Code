/*
========================================
SERVER.JS — MAIN SERVER FILE
========================================

PROJECT GOAL:
You are building a basic server-side JavaScript project.
This server will:
1. Run using Node.js
2. Call an external API (any API you choose)
3. Expose your OWN API endpoint

========================================
NODE.JS INSTALLATION (DO THIS FIRST)
========================================

Node.js allows JavaScript to run outside the browser.

INSTALL STEPS:
1. Go to https://nodejs.org
2. Download the version labeled "LTS (Recommended)"
3. Run the installer
4. Click Next on all steps and keep default settings
5. Finish installation

VERIFY INSTALLATION:
Open a terminal and run:
  node -v
  npm -v

If you see version numbers, Node.js is installed correctly.

If it does not work:
- Restart your computer
- Open a NEW terminal
- Try again

========================================
PROJECT SETUP
========================================

In this project folder, run these commands:

1. npm init -y
2. npm install express
3. node server.js

Then open a browser and visit:
http://localhost:3000/api/data

RULES:
- You may ONLY use server.js and script.js
- Do not add more files
*/

// Import Express
const express = require("express");
const app = express();
const PORT = 3000;

// Import API logic from script.js
const fetchFromAPI = require("./script");

/*
----------------------------------------
ROOT ROUTE
----------------------------------------
Used only to confirm the server is running.
*/
app.get("/", (req, res) => {
	res.send("Server is running");
});

/*
----------------------------------------
API ROUTE
----------------------------------------
This is YOUR API endpoint.

When visiting:
http://localhost:3000/api/data

The server will:
1. Call the external API
2. Wait for the response
3. Return the data as JSON
*/
app.get("/api/data", async (req, res) => {
	try {
		const data = await fetchFromAPI();
		res.json(data);
	} catch (error) {
		res.status(500).json({
			error: "Failed to fetch data from external API",
		});
	}
});

/*
----------------------------------------
START SERVER
----------------------------------------
If you see the message below in the terminal,
your server is running correctly.
*/
app.listen(PORT, () => {
	console.log(`Server running at http://localhost:${PORT}`);
});

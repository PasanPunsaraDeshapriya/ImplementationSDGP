const express = require('express');
const bodyParser = require('body-parser');
const { PythonShell } = require('python-shell');
const mime = require('mime');
const app = express();
app.use(bodyParser.urlencoded({extended : true}))
const port = 3000;

// Serve the index.html file
app.get('/', function(req, res) {
  res.sendFile(__dirname + '/test.html');
});
//
// Handle POST requests to the /predict endpoint
app.post('/', function(req, res) {
  // Parse the input data from the request body
  var inputData = req.body.oneth;
  console.log(inputData);

  // Set up the Python shell options
  var options = {
    scriptPath: __dirname + '/python',
    args: inputData
  };

  // Run the Python script
  PythonShell.run('app.py', options, function(err, result) {
    if (err) {
      console.error(err);
      res.status(500).send("Internal server error");
      return;
    }

    // Parse the predicted output from the Python script
    try {
      var outputData = JSON.parse(result[0]);
    } catch (e) {
      console.error(e);
      res.status(500).send("Error parsing output from Python script");
      return;
    }

    // Send the predicted output back to the client as JSON
    res.json(outputData);
  });
});

// Start the server
app.listen(port, function() {
  console.log('Server is running on port', port);
});

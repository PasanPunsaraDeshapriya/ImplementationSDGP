const express = require('express');
const bodyParser = require('body-parser');
const { PythonShell } = require('python-shell');

const app = express();
const port = 3000;

// Serve the index.html file
app.get('/', function(req, res) {
  res.sendFile(__dirname + '/careerFinderModel.html');
});

// Handle POST requests to the /predict endpoint
app.post('/predict', function(req, res) {
  // Parse the input data from the request body
  var inputData = req.body;

  // Set up the Python shell options
  var options = {
    scriptPath: __dirname + '/python',
    args: [inputData]
  };

  // Run the Python script
  PythonShell.run('app.py', options, function(err, result) {
    if (err) throw err;

    // Parse the predicted output from the Python script
    var outputData = JSON.parse(result[0]);

    // Send the predicted output back to the client as JSON
    res.json(outputData);
  });
});

// Start the server
app.listen(port, function() {
  console.log('Server is running on port', port);
});

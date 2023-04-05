const http = require('http');
const fs = require('fs');
const csv = require('csv-parser');

const server = http.createServer(function(req, res) {
  if (req.url === '/') {
    // Read the career pathways from the CSV file
    const iT = [];
    const marketing = [];
    const creative = [];
    const healthcare = [];
    const education = [];
    fs.createReadStream('datasets/information-tech.csv')
      .pipe(csv())
      .on('data', (data) => {
        iT.push(data[Object.keys(data)[0]]);
      })
    fs.createReadStream('datasets/education.csv')
      .pipe(csv())
      .on('data', (data) => {
        education.push(data[Object.keys(data)[0]]);
      })
    fs.createReadStream('datasets/marketing.csv')
      .pipe(csv())
      .on('data', (data) => {
        marketing.push(data[Object.keys(data)[0]]);
      })
    fs.createReadStream('datasets/healthcare.csv')
      .pipe(csv())
      .on('data', (data) => {
        healthcare.push(data[Object.keys(data)[0]]);
      })
    fs.createReadStream('datasets/creative-arts.csv')
      .pipe(csv())
      .on('data', (data) => {
        creative.push(data[Object.keys(data)[0]]);
      })
      .on('end', () => {
        // Read the HTML template from a file
        fs.readFile('test.html', 'utf8', function(err, html) {
          if (err) {
            throw err;
          }

          // Generate the select element HTML using the career pathways
          let selectiT = '<select id="iT">';
          for (let i = 0; i < 50; i++) {
            selectiT += `<option value="${i}">${iT[i]}</option>`;
          }
          selectiT += '</select>';

          let selectEducation = '<select id="education">';
          for (let i = 0; i < 50; i++) {
            selectEducation += `<option value="${i}">${education[i]}</option>`;
          }
          selectEducation += '</select>';

          let selectMarketing = '<select id="marketing">';
          for (let i = 0; i < 50; i++) {
            selectMarketing += `<option value="${i}">${marketing[i]}</option>`;
          }
          selectMarketing += '</select>';

          let selectCreative = '<select id="creative">';
          for (let i = 0; i < 50; i++) {
            selectCreative += `<option value="${i}">${creative[i]}</option>`;
          }
          selectCreative += '</select>';

          let selectHealthcare = '<select id="healthcare">';
          for (let i = 0; i < 50; i++) {
            selectHealthcare += `<option value="${i}">${healthcare[i]}</option>`;
          }
          selectHealthcare += '</select>';

          // Replace the placeholder in the HTML template with the select element HTML
          const finalHTML = html.replace('{{iT}}', selectiT).replace('{{education}}', selectEducation).replace('{{marketing}}', selectMarketing).replace('{{healthcare}}', selectHealthcare).replace('{{creative}}', selectCreative);
          // Send the final HTML page to the client
          res.writeHead(200, {
            'Content-Type': 'text/html'
          });
          res.write(finalHTML);
          res.end();
        });
      });

  } else {
    // Return a 404 error for any other requests
    res.writeHead(404);
    res.end();
  }
});

server.listen(3000, function() {
  console.log('Server is listening on port 3000');
})

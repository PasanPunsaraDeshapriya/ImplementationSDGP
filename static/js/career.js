var newNumber;
console.log("file is working");
$(document).ready(function() {
  $("#submit").click(function() {
    var r = 0;
    var i = 0;
    var a = 0;
    var s = 0;
    var e = 0;
    var c = 0;
    // Get the selected answer for question 1
    var q1 = $('input[name="q1"]:checked').val();

    // Get the selected answer for question 2
    var q2 = $('input[name="q2"]:checked').val();

    var q3 = $('input[name="q3"]:checked').val();

    var q4 = $('input[name="q4"]:checked').val();

    var q5 = $('input[name="q5"]:checked').val();

    var q6 = $('input[name="q6"]:checked').val();

    var q7 = $('input[name="q7"]:checked').val();

    var q8 = $('input[name="q8"]:checked').val();

    var q9 = $('input[name="q9"]:checked').val();

    var q10 = $('input[name="q10"]:checked').val();

    var q11 = $('input[name="q11"]:checked').val();

    var q12 = $('input[name="q12"]:checked').val();

    var q13 = $('input[name="q13"]:checked').val();

    var q14 = $('input[name="q14"]:checked').val();

    var q15 = $('input[name="q15"]:checked').val();

    var q16 = $('input[name="q16"]:checked').val();

    var q17 = $('input[name="q17"]:checked').val();

    var q18 = $('input[name="q18"]:checked').val();

    var q19 = $('input[name="q19"]:checked').val();

    var q20 = $('input[name="q20"]:checked').val();

    var q21 = $('input[name="q21"]:checked').val();

    var q22 = $('input[name="q22"]:checked').val();

    var q23 = $('input[name="q23"]:checked').val();

    var q24 = $('input[name="q24"]:checked').val();

    var q25 = $('input[name="q25"]:checked').val();

    var q26 = $('input[name="q26"]:checked').val();

    var q27 = $('input[name="q27"]:checked').val();

    var q28 = $('input[name="q28"]:checked').val();

    var q29 = $('input[name="q29"]:checked').val();

    var q30 = $('input[name="q30"]:checked').val();

    var q31 = $('input[name="q31"]:checked').val();

    var q32 = $('input[name="q32"]:checked').val();

    var q33 = $('input[name="q33"]:checked').val();

    var q34 = $('input[name="q34"]:checked').val();

    var q35 = $('input[name="q35"]:checked').val();

    var q36 = $('input[name="q36"]:checked').val();

    var q37 = $('input[name="q37"]:checked').val();

    var q38 = $('input[name="q38"]:checked').val();

    var q39 = $('input[name="q39"]:checked').val();

    var q40 = $('input[name="q40"]:checked').val();

    var q41 = $('input[name="q41"]:checked').val();

    var q42 = $('input[name="q42"]:checked').val();


    // Check if both questions are answered
    if (q1 === undefined || q2 === undefined || q3 === undefined) {
      $("#result").text("Please answer answer all questions.");
    } else {
      // Check the answers
      var correct = 0;
      if (q1 === "yes") {
        r++;
      }
      if (q2 === "yes") {
        i++;
      }
      if (q3 === "yes") {
        a++;
      }
      if (q4 === "yes") {
        s++;
      }
      if (q5 === "yes") {
        e++;
      }
      if (q6 === "yes") {
        c++;
      }
      if (q7 === "yes") {
        r++;
      }
      if (q8 === "yes") {
        a++;
      }
      if (q9 === "yes") {
        c++;
      }
      if (q10 === "yes") {
        e++;
      }
      if (q11 === "yes") {
        i++;
      }
      if (q12 === "yes") {
        s++;
      }
      if (q13 === "yes") {
        s++;
      }
      if (q14 === "yes") {
        r++;
      }
      if (q15 === "yes") {
        c++;
      }
      if (q16 === "yes") {
        e++;
      }
      if (q17 === "yes") {
        a++;
      }
      if (q18 === "yes") {
        i++;
      }
      if (q19 === "yes") {
        e++;
      }
      if (q20 === "yes") {
        s++;
      }
      if (q21 === "yes") {
        i++;
      }
      if (q22 === "yes") {
        r++;
      }
      if (q23 === "yes") {
        a++;
      }
      if (q24 === "yes") {
        c++;
      }
      if (q25 === "yes") {
        c++;
      }
      if (q26 === "yes") {
        i++;
      }
      if (q27 === "yes") {
        a++;
      }
      if (q28 === "yes") {
        s++;
      }
      if (q29 === "yes") {
        e++;
      }
      if (q30 === "yes") {
        r++;
      }
      if (q31 === "yes") {
        a++;
      }
      if (q32 === "yes") {
        r++;
      }
      if (q33 === "yes") {
        i++;
      }
      if (q34 === "yes") {
        s++;
      }
      if (q35 === "yes") {
        c++;
      }
      if (q36 === "yes") {
        e++;
      }
      if (q37 === "yes") {
        r++;
      }
      if (q38 === "yes") {
        c++;
      }
      if (q39 === "yes") {
        i++;
      }
      if (q40 === "yes") {
        s++;
      }
      if (q41 === "yes") {
        a++;
      }
      if (q42 === "yes") {
        c++;
      }

      let numbers = [
        [r, "r"],
        [i, "i"],
        [a, "a"],
        [s, "s"],
        [e, "e"],
        [c, "c"]
      ];

      // Sort the array in descending order
      numbers.sort(function(a, b) {
        return b[1] - a[1];
      });

      // Print the highest three numbers
      console.log("The highest three numbers are: " + numbers[0][0] + " " + numbers[0][1] + " , " + numbers[1][0] + " " + numbers[1][1] + " , " + numbers[2][0] + " " + numbers[2][1]);
      newNumber = numbers[0][1]+numbers[1][1]+numbers[2][1];
      console.log(newNumber);
      // fetch('http://localhost:8000/dataset.csv')
      //   .then(response => response.text())
      //   .then(data => {
      //     // Parse the CSV data
      //     const rows = data.split('\n').map(row => row.split(','));
      //     console.log(rows);
      //   })
      //   .catch(error => console.error(error));

      // Display the result
      $("#result").text("the pathway number you got is " + newNumber);
    }
  });
})

$(document).ready(function() {
  $("#submit2").click(function() {
      var myData = newNumber;

      $.ajax({
          type: "POST",
          url: "/my-python-endpoint2",
          data: JSON.stringify(myData),
          success: function(response) {
              console.log("Data sent to Python:", response);
          },
          contentType: "application/json",
          dataType: "json"
      });
  });
});
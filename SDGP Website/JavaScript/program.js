$(document).ready(function() {
  $("#submit").click(function() {
    var r=0;
    var i=0;
    var a=0;
    var s=0;
    var e=0;
    var c=0;
    // Get the selected answer for question 1
    var q1 = $('input[name="q1"]:checked').val();

    // Get the selected answer for question 2
    var q2 = $('input[name="q2"]:checked').val();

    var q3 = $('input[name="q3"]:checked').val();

    var q4 = $('input[name="q4"]:checked').val();

    var q5 = $('input[name="q5"]:checked').val();

    var q6 = $('input[name="q6"]:checked').val();

    // Check if both questions are answered
    if (q1 === undefined || q2 === undefined || q3 === undefined ) {
      $("#result").text("Please answer both questions.");
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

      // Display the result
      $("#result").text("You got r as " + r + " i as " + i + " a as " + a + " s as " + s + " e as " + e + " c as " + c);
    }
  });
})

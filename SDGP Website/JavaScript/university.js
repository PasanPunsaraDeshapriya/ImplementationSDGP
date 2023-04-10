const selectElement = document.getElementById("provinces");
const selectedValue = selectElement.value;
console.log(selectedValue)

const element1 = document.getElementById("foreign");
const selectedValue1 = element1.value;
console.log(selectedValue1)

$(document).ready(function() {
  $("input[name='size']").change(function() {
    const selectedValue = $("input[name='size']:checked").val();
    console.log(selectedValue);
  });
});

$(document).ready(function() {
  $("input[name='program']").change(function() {
    const selectedValue = $("input[name='program']:checked").val();
    console.log(selectedValue);
  });
});


$(document).ready(function() {
  $("input[name='budget']").change(function() {
    const selectedValue = $("input[name='budget']:checked").val();
    console.log(selectedValue);
  });
});

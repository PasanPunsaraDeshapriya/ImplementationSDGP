$(document).ready(function() {
  $("#provinces").change(function province() {
    return $(this).val();
    console.log(selectedValue);
  });
});

$(document).ready(function() {
  $("#foreign").change(function foreign() {
    const selectedValue1 = $(this).val();
    console.log(selectedValue1);
  });
});

$(document).ready(function size() {
  $("input[name='size']").change(function() {
    const selectedValue2 = $("input[name='size']:checked").val();
    console.log(selectedValue2);
  });
});

$(document).ready(function program() {
  $("input[name='program']").change(function() {
    const selectedValue3 = $("input[name='program']:checked").val();
    console.log(selectedValue3);
  });
});

$(document).ready(function budget() {
  $("input[name='budget']").change(function() {
    const selectedValue4 = $("input[name='budget']:checked").val();
    console.log(selectedValue4);
  });
});

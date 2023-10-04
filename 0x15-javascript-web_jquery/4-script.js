$(document).ready(function () {
  const toggleheader = $('DIV#toggle_header');
  const headerElement = $('header');
  toggleheader.click(function () {
    headerElement.toggleClass('red green');
  });
});

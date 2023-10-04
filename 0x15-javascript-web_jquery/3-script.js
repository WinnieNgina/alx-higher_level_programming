$(document).ready(function () {
  const redHeader = $('DIV#red_header');
  redHeader.click(function () {
    const headerElement = $('header');
    headerElement.addClass('red');
  });
});

(function() {
function throttle(func, delay) {
  var tick;

  return function() {
    var args = arguments;
    if (tick) window.clearTimeout(tick);

    tick = window.setTimeout(function() {
      tick = null;
      func.apply(func, arguments);
    }, delay);
  }
}

function updatePreview() {
  var $ = document.getElementById.bind(document);
  var title = $('titleInput').value;
  var body = $('bodyInput').value;
  $('bodyOutput').innerHTML = markdown.toHTML(body);
  $('titleOutput').innerHTML = title;
}

function updatePreviewOn(elem) {
  // Update on changes to this element
  elem.addEventListener('keydown', throttle(updatePreview, 500));
}

updatePreviewOn(document.getElementById('bodyInput'))
updatePreviewOn(document.getElementById('titleInput'))
})();

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

function preview(inElem, outElem) {
  function md() {
    outElem.innerHTML = markdown.toHTML(inElem.value);
  }
  inElem.addEventListener('keydown', throttle(md, 500));
}

preview(document.getElementById('input'), document.getElementById('output'));
})();

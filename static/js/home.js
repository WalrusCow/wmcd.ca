(function() {
  var tabDisplays = [];
  var currentTab = document.getElementsByClassName('defaultTab')[0];

  function switchTabs(from, to) {
    from.style.display = 'none';
    to.style.display = 'block';
  }

  function attachControl(control, display) {
    control.addEventListener('click', function() {
      switchTabs(currentTab, display);
      currentTab = display;
    });
  }

  function getChildren(node) {
    var children = [];
    for (var i = 0; i < node.childNodes.length; ++i) {
      if (node.childNodes[i].nodeType === Node.ELEMENT_NODE)
        children.push(node.childNodes[i]);
    }
    return children;
  }

  function init() {
    var tabContainer = document.getElementById('tabContainer');
    var controlContainer = document.getElementById('controlContainer');

    tabDisplays = getChildren(tabContainer);
    var tabControls = getChildren(controlContainer);

    for (var i = 0; i < tabControls.length; ++i) {
      attachControl(tabControls[i], tabDisplays[i]);
    }
  }

  init();
})();

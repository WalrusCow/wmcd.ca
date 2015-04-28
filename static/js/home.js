(function() {
  var tabDisplays = [];
  var tabControls = [];
  var currentTab = document.getElementsByClassName('tab-center')[0];
  var $highlight = $('.tab-control-highlight');

  function switchTabs(from, to) {
    var $to = $(to);
    var $from = $(from);
    $to.removeClass('tab-right')
       .removeClass('tab-left')
       .addClass('tab-center');

    $from.removeClass('tab-center');
    var before = true;

    var left = 0;
    var idx = 0;
    for (var i = 0; i < tabDisplays.length; ++i) {
      if (tabDisplays[i] === to) {
        before = false;
        idx = i;
        continue;
      }
      $(tabDisplays[i]).addClass(before ? 'tab-left' : 'tab-right')
                       .removeClass(before ? 'tab-right' : 'tab-left');
      if (before) {
        left += $(tabControls[i]).outerWidth();
      }
    }
    var width = $(tabControls[idx]).outerWidth();
    $highlight.css('left', left);
    $highlight.css('width', width);
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
    var tabContainer = document.getElementById('tab-container');
    var controlContainer = document.getElementById('control-container');

    tabDisplays = getChildren(tabContainer);
    tabControls = getChildren(controlContainer);

    for (var i = 0; i < tabControls.length; ++i) {
      attachControl(tabControls[i], tabDisplays[i]);
    }
  }

  init();
})();

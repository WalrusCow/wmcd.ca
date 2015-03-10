(function() {
  requirejs.config({
    baseUrl: '/js/tetvas',
    paths: { 'require': '..' }
  });

  requirejs(['tetvas'], function(Tetvas) {
    new Tetvas();
  });
})();

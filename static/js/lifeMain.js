(function() {
  requirejs.config({
    baseUrl: '/js',
    paths: { 'require': '.', }
  });

  requirejs(['life/life'], function(Life) {
    new Life();
  });
})();

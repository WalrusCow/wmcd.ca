define(function() {
  /* Written for use with require.js */

  // Return object
  var sg = {};

  sg.GameGrid = function (options) {
    /*
     * Return a Block class for a grid with specified options.
     *
     * Options:
     *  - ctx:        Canvas context to draw on
     *  - squareSize: Size of each square in the grid
     *  - offset:     Amount to offset the drawing by on the canvas. Should
     *                have `x` and `y` attributes.  Defaults to 0.
     */

    // Allow these to be accessed by the Block class
    var ctx = options.ctx;
    var squareSize = options.squareSize;
    var offset = options.offset || { x: 0, y: 0 };

    function drawSquare(coords, size, fill) {
      ctx.fillStyle = fill;
      ctx.fillRect(coords.x, coords.y, size, size);
    }

    function Block(coords, options) {
      /*
       * Options:
       *  - fill
       *  - hasBorder
       *  - borderSize
       *  - borderFill
       */

      this.coords = {
        x: coords.x,
        y: coords.y
      };

      // Real coordinates in pixels
      this._pxCoords = {
        x: coords.x * squareSize + offset.x,
        y: coords.y * squareSize + offset.y
      };

      // Set all options (but don't overwrite existing properties)
      for (var key in options) {
        if (!(this[key] || Block.prototype[key])) {
          this[key] = options[key];
        }
      }

    }

    Block.prototype.draw = function() {
      /* Draw the block. */

      // No border - simple drawing
      if (!this.hasBorder) {
        drawSquare(this._pxCoords, squareSize, this.fill);
        return;
      }

      // Draw border (middle will be filled with fill)
      drawSquare(this._pxCoords, squareSize, this.borderFill);

      // Coords of inside are shifted by border size
      var insideCoords = {
        x: this._pxCoords.x - this.borderSize,
        y: this._pxCoords.y - this.borderSize
      };
      // Size of inside is shrunk by twice border size
      var insideSize = squareSize - 2 * this.borderSize;

      // Draw fill
      drawSquare(insideCoords, insideSize, this.fill);
    };

    Block.prototype.undraw = function() {
      /* Undraw the block. */
      ctx.clearRect(this._pxCoords.x, this._pxCoords.y, squareSize, squareSize);
    };

    // Return the class that can be used for the grid
    return Block;
  }

  sg.registerControls = function(game, controls, sel) {
    /*
     * Register controls for a game (as handlers).
     *
     * Arguments:
     *  - game: Object (game) to save control objects to.  Controls are called
     *  with game as `this`.
     *  - controls: Array of controls to register.  Each control should have
     *  - sel: Prepended to id when searching for the element for a control.
     *  Elements are searched for by id attribute.
     *  elements:
     *    + id: game[id + 'Control'] is set to the event listener
     *    + event: event to listen to
     *    + handler: handler to be called with the event when it is triggered
     *
     * Note: Events are propagated up.
     */

    for(var i = 0; i < controls.length; ++i) {
      var control = controls[i];

      // Control element
      var el = document.getElementById(sel + control.id);
      game[control.id + 'Control'] = el;
      el.addEventListener(control.event, control.handler.bind(game));
    };

  };

  sg.copyPoint = function(pt) {
    return { x: pt.x, y: pt.y };
  };

  sg.addPoints = function(pt1, pt2) {
    /* Return a new point by summing the coordinates of the input points. */
    return {
      x: pt1.x + pt2.x,
      y: pt1.y + pt2.y
    };
  };

  sg.pointsEqual = function(pt1, pt2) {
    /* Checks if points are equal. */
    return (pt1.x === pt2.x) && (pt1.y === pt2.y);
  };

  sg.randInt = function(min, max) {
    /* Generate a random integer in the interval [min, max). */
    return Math.floor(Math.random() * (max - min)) + min;
  };

  return sg;
});

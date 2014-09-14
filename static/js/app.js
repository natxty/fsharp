/*!
 * jQchx scripts ... 
 * Nathaniel Clark :: @natxty
 */

var jqchx = (function () {
    var self = {},
    debug = true;


    /* ============================================================================== */
    /* Helper functions
    /* ============================================================================== */
    function _log(str) {
        if(debug) console.log(str);
    }

    /* ============================================================================== */
    /* Main FORM Function
    /* ============================================================================== */
    $('#jqchx_form').submit(function(e) {
        e.preventDefault();
        var url = $('#jqchx_form #inputurl').val()
        $(this).find('input[type="submit"]').attr('disabled','disabled');
        $('.messaging h3').html('Searching...');

        // make sure we've got the http?? 

        //then, submit     
        $.ajax({
          type: "POST",
          url: '/jqchx',
          data: { url: url },
          success: function(data) {
            $('.messaging h3').html(data);
          },
          error: function(data) {
            $('.messaging h3').html('There was an error from the server');
          }
        });


    })

    /* ============================================================================== */
    /* initialization
    /* ============================================================================== */
    self.init = function () {


    }

    return self;
}());
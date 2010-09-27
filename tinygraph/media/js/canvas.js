$(function() {
    
    // var editing = false;
    // var $editBar = $('#canvas-wrapper #edit-bar');
    // var $editToggleButton = $('#canvas-wrapper #edit-mode-button');
    // 
    // $editBar.hide();
    
    $('#edit-mode-button').hide();
    
    // $editToggleButton.click(function() {
    //     if(editing) {
    //         $editBar.removeClass('enabled').slideUp(100);
    //         $editToggleButton.removeClass('enabled');
    //         editing = false;
    //     } else {
    //         $editBar.addClass('enabled').slideDown(100);
    //         $editToggleButton.addClass('enabled');
    //         editing = true;
    //     }
    // });
    
    var $canvas = $('#canvas');
    var $wrapper = $canvas.parent();
    
    // function resize($elem) {
    //     var $parent = $elem.parent();
    //     $elem.width($parent.width())
    //          .height($parent.height());
    // }
    
    $("#task-bar a").click(function() {
        return false;
    });
    
    $('#form_new_host_submit').click(function() {
        $('#form_new_host').submit();
    });
    
    $('#form_new_host').submit(function() {
        
        var data = $(this).serialize();
        $(this).children().attr('disabled', 'disabled');
        $canvas.html('<p>loading ...</p>');
        $.ajax({
            url: window.location,
            type: 'POST',
            data: data,
            success: function(html) {
                $canvas.html(html);
                $('#form_new_host').children().removeAttr('disabled');
            }
        });
        
        return false;
    });
});
(function($) {
    $(document).ready(function() {
        $.fn.loadChainedChoices = function() {
            var chained_id = $(this).attr('chained_id');
            if (chained_id.indexOf('__prefix__') != -1) {
                chained_id = chained_id.replace('__prefix__', $(this).attr('name').split('-')[1]);
                $(this).attr('chained_id', chained_id);
            }

            var valuefield = $('#' + chained_id);
            var ajax_url = valuefield.attr('ajax_url');

            $.get(ajax_url, {field: valuefield.attr('name').split('-')[2], parent_value: $(this).val()}, function(j) {
                var options = '';
                for (var i = 0; i < j.length; i++) {
                    options += '<option value="' + j[i][0] + '">' + j[i][1] + '</option>';
                }
                valuefield.html(options);
                valuefield.trigger('change');
            }, "json");
        }

        $('.chained-parent-field').live('change', function(e) {
            $(this).loadChainedChoices();
        });
    });
})(django.jQuery);





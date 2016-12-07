/**
 * Created by lianliang on 16/8/28.
 */

(function (jq) {
    jq.extend({
        'test': function(arg) {
            console.log(arg);
        }
    });
    jq.fn.extend({
        'test1': function () {
            // this 表示选择器对应的元素
            console.log(this);
        }

    });
})(jQuery);
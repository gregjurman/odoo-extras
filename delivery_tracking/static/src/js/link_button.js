(function() {
        var instance = openerp;
	var _t = instance.web._t,
	_lt = instance.web._lt,
	QWeb = instance.web.qweb;
instance.web.list.TrackingButton = instance.web.list.Column.extend({
    /**
 * Return an actual ``<button>`` tag
 */
    _format: function (row_data, options) {
	return _.str.sprintf(row_data['carrier_track_url'].value ? '<a href="%s" class="oe_button" target="new">Track Delivery</a>': '', row_data['carrier_track_url'].value);
    }
});
	instance.web.list.columns.add('field.tracking_button', 'instance.web.list.TrackingButton');
})()

$(document).ready(function(){
	$(function(){
		showMap(114.414091,30.481263);
	})

	function showMap(x, y) { 
		var map = new BMap.Map("mymap");
		map.centerAndZoom(new BMap.Point(x, y), 15);
		map.addControl(new BMap.NavigationControl());
		var content = '<div style="margin:0;line-height:20px;padding:2px;">'+
		            '电  话：15871722717<br/>邮  箱：15871722717@163.com<br/>地 址：武汉市东湖高新技术开发区武大科技园二路宏业楼一楼<br/>' +
		          '</div>';
		var searchInfoWindow = new BMapLib.SearchInfoWindow(map, content, {
		title: "公司信息", //标题
		width: 300, //宽度
		height: 100, //高度
		panel : "panel", //检索结果面板
		enableAutoPan : true, //自动平移
		searchTypes :[
		]
		});
		var marker = new BMap.Marker(new BMap.Point(x, y));
		searchInfoWindow.open(marker);
		map.addOverlay(marker);

	}
});
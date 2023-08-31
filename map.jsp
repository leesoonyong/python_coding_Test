<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%-- <%@ include file="/WEB-INF/views/includes.jsp" %> --%>
<script src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>
<script>
	function initialize() {
		/*지도 오류(회사가 판교로 이사가서 구글맵이 이상하게뜨므로 주석처리)
		var Y_point			= 37.411482;		// Y 좌표
		var X_point			= 127.095546;		// X 좌표

		var zoomLevel		= 16;						// 지도의 확대 레벨 : 숫자가 클수록 확대정도가 큼

		var markerTitle		= "(주)아와소프트";				// 현재 위치 마커에 마우스를 오버을때 나타나는 정보
		var markerMaxWidth	= 350;						// 마커를 클릭했을때 나타나는 말풍선의 최대 크기

		// 말풍선 내용
		var contentString	= '<div>' +
		'<h2>(주)아와소프트</h2>'+
		'</div>';

		var myLatlng = new google.maps.LatLng(Y_point, X_point);
		var mapOptions = {
							zoom: zoomLevel,
							center: myLatlng,
							mapTypeId: google.maps.MapTypeId.ROADMAP
		}
		var map = new google.maps.Map(document.getElementById('map_view'), mapOptions);

		var marker = new google.maps.Marker({
												position: myLatlng,
												map: map,
												title: '(주)아와소프트'
		});

		var infowindow = new google.maps.InfoWindow(
													{
														content: contentString,
														maxWidth: markerMaxWidth
													}
		);
		infowindow.open(map, marker);
		*/
	}
</script>
<main id="main" class="main customer_wrap">
	<div class="main_header">
		<h3>오시는길</h3>
	</div>
	<div class="main_linemap">
		<ul>
			<li><a href="/" class="linemap_home blind">홈</a></li>
			<li>
				<span>소통과 협력</span>
				<ul class="linemap_sub">
					<li><a href="/home/company/introduce">회사소개</a></li>
					<li><a href="/home/product/deepLearning">사업분야</a></li>
					<li><a href="/home/customer/client" class="on">소통과 협력</a></li>
				</ul>
			</li>
			<li>
				<span>오시는길</span>
				<ul class="linemap_sub">
					<li><a href="/home/customer/client">고객사</a></li>
					<li><a href="/home/customer/recruitInfo">인재채용</a></li>
					<li><a href="/home/customer/rule">윤리경영</a></li>
					<li><a href="/home/customer/map" class="on">오시는길</a></li>
				</ul>
			</li>
		</ul>
	</div>
	<div class="container">
		<div class="inner company_07">
			<div class="company_map">
				<div id="map_view" class="map_view">
					<img src="/images/customer/map.png">
				</div>
				<div class="map_info">
					<div class="location">
						<h4>주식회사 아와소프트</h4>
						<span>
						<br>(우)13449 경기도 성남시 수정구 창업로 43(판교글로벌비즈센터 B동 812호, 813호)</span>
						<!-- 추후 내용 더 필요할  경우 여기에 추가<i>분당선 야탑역 2번 출구 50미터</i> -->
					</div>
				</div>
				<div class="map_info">
					<ul>
						<li>
							<span class="email"><a href="mailto:recruit@awasoft.co.kr">recruit@awasoft.co.kr</a></span>
						</li>
						<li>
							<span class="tel"><a href="tel:070-4355-5387">070 - 4355 - 5387</a></span>
						</li>
						<li>
							<span class="fax">031 - 8016 - 3229</span>
						</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</main>
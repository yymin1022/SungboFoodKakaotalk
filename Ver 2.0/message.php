<?php
	$data = json_decode(file_get_contents('php://input'), true);
	$content = $data["content"];
	$time = time();
	
	switch($content){
		case "오늘중식":
			$date = date("Y.m.d", strtotime("+9 hours", $time));
			$URL="http://juneyoung.kr/api/school-meal/meal_api_custom.php?countryCode=stu.sen.go.kr&schulCode=B100000470&insttNm=성보고등학교&schulCrseScCode=4&schMmealScCode=2&schYmd=" . $date;
			$ch = curl_init();
			curl_setopt ($ch, CURLOPT_URL, $URL);
			curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
			$file_contents = curl_exec($ch);
		
			$json = json_decode($file_contents, true);
			$lunch = $date.'.\n성보고등학교 중식\n'.$json['메뉴'];
			
			echo '
				{
					"message":
					{
						"text" : "'.str_replace("(중식)", "", $lunch).'"
					},
					"keyboard":
					{
						"type" : "buttons",
						"buttons" : ["오늘중식", "오늘석식"]
					}
				}';
			break;
		case "오늘석식":
			$date = date("Y.m.d", strtotime("+9 hours", $time));
			$URL="http://juneyoung.kr/api/school-meal/meal_api_custom.php?countryCode=stu.sen.go.kr&schulCode=B100000470&insttNm=성보고등학교&schulCrseScCode=4&schMmealScCode=3&schYmd=" . $date;
			$ch = curl_init();
			curl_setopt ($ch, CURLOPT_URL, $URL);
			curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
			$file_contents = curl_exec($ch);
		
			$json = json_decode($file_contents, true);
			$dinner = $date.'.\n성보고등학교 석식\n'.$json['메뉴'];
			
			echo '
				{
					"message":
					{
						"text" : "'.$dinner.'"
					},
					"keyboard":
					{
						"type" : "buttons",
						"buttons" : ["오늘중식", "오늘석식"]
					}
				}';
			break;
	}	
?>
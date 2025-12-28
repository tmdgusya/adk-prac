블로그 검색 결과 조회 
설명 
네이버 검색의 블로그 검색 결과를 XML 형식 또는 JSON 형식으로 반환합니다.

요청 URL 
요청 URL	결괏값 반환 형식
https://openapi.naver.com/v1/search/blog.xml	XML
https://openapi.naver.com/v1/search/blog.json	JSON
프로토콜 
HTTPS

HTTP 메서드 
GET

파라미터 
파라미터를 쿼리 스트링 형식으로 전달합니다.

파라미터	타입	필수 여부	설명
query	String	Y	검색어. UTF-8로 인코딩되어야 합니다.
display	Integer	N	한 번에 표시할 검색 결과 개수(기본값: 10, 최댓값: 100)
start	Integer	N	검색 시작 위치(기본값: 1, 최댓값: 1000)
sort	String	N	검색 결과 정렬 방법
- sim: 정확도순으로 내림차순 정렬(기본값)
- date: 날짜순으로 내림차순 정렬
참고 사항 
API를 요청할 때 다음 예와 같이 HTTP 요청 헤더에 클라이언트 아이디와 클라이언트 시크릿을 추가해야 합니다.

> GET /v1/search/blog.xml?query=%EB%A6%AC%EB%B7%B0&display=10&start=1&sort=sim HTTP/1.1
> Host: openapi.naver.com
> User-Agent: curl/7.49.1
> Accept: */*
> X-Naver-Client-Id: {애플리케이션 등록 시 발급받은 클라이언트 아이디 값}
> X-Naver-Client-Secret: {애플리케이션 등록 시 발급받은 클라이언트 시크릿 값}
>
요청 예 
curl  "https://openapi.naver.com/v1/search/blog.xml?query=%EB%A6%AC%EB%B7%B0&display=10&start=1&sort=sim" \
    -H "X-Naver-Client-Id: {애플리케이션 등록 시 발급받은 클라이언트 아이디 값}" \
    -H "X-Naver-Client-Secret: {애플리케이션 등록 시 발급받은 클라이언트 시크릿 값}" -v
응답 
응답에 성공하면 결괏값을 XML 형식 또는 JSON 형식으로 반환합니다. XML 형식의 결괏값은 다음과 같습니다.

요소	타입	설명
rss	-	RSS 컨테이너. RSS 리더기를 사용해 검색 결과를 확인할 수 있습니다.
rss/channel	-	검색 결과를 포함하는 컨테이너. channel 요소의 하위 요소인 title, link, description은 RSS에서 사용하는 정보이며, 검색 결과와는 상관이 없습니다.
rss/channel/lastBuildDate	dateTime	검색 결과를 생성한 시간
rss/channel/total	Integer	총 검색 결과 개수
rss/channel/start	Integer	검색 시작 위치
rss/channel/display	Integer	한 번에 표시할 검색 결과 개수
rss/channel/item	-	개별 검색 결과. JSON 형식의 결괏값에서는 items 속성의 JSON 배열로 개별 검색 결과를 반환합니다.
rss/channel/item/title	String	블로그 포스트의 제목. 제목에서 검색어와 일치하는 부분은 <b> 태그로 감싸져 있습니다.
rss/channel/item/link	String	블로그 포스트의 URL
rss/channel/item/description	String	블로그 포스트의 내용을 요약한 패시지 정보. 패시지 정보에서 검색어와 일치하는 부분은 <b> 태그로 감싸져 있습니다.
rss/channel/item/bloggername	String	블로그 포스트가 있는 블로그의 이름
rss/channel/item/bloggerlink	String	블로그 포스트가 있는 블로그의 주소
rss/channel/item/postdate	dateTime	블로그 포스트가 작성된 날짜
응답 예 
< HTTP/1.1 200 OK
< Server: nginx
< Date: Mon, 26 Sep 2016 01:39:37 GMT
< Content-Type: text/xml;charset=utf-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< Keep-Alive: timeout=5
< Vary: Accept-Encoding
< X-Powered-By: Naver
< Cache-Control: no-cache, no-store, must-revalidate
< Pragma: no-cache
<
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
    <channel>
        <title>Naver Open API - blog ::'리뷰'</title>
        <link>http://search.naver.com</link>
        <description>Naver Search Result</description>
        <lastBuildDate>Mon, 26 Sep 2016 10:39:37 +0900</lastBuildDate>
        <total>8714891</total>
        <start>1</start><display>10</display>
        <item>
            <title>명예훼손 없이 <b>리뷰</b>쓰기</title>
            <link>http://openapi.naver.com/l?AAABWLyw6CMBREv+ayNJe2UrrogvJwg8aYKGvACiSUalNR/t6azGLO5Mzrrd0moVSQJZDl/6I4KIxGpx9y9P4JNANShXSzHXZLu2q3660Jw2bt0k1+aF1rgFYXfZ+c7j3QorYDkCT4JxuIEEyRUYGcxpGXMeMs3VPBOUEWGXntynUW03k7ohBYfG+mOdRqbPL6E84/apnqgaEAAAA=</link>
            <description>명예훼손 없이 <b>리뷰</b>쓰기 우리 블로그하시는 분들께는 꽤 중요한 내용일 수도 있습니다 그것도 주로 <b>리뷰</b> 위주로 블로그를 진행하신 분이라면 더욱 더 말이죠
                오늘 포스팅은, 어떻게 하면 객관적이고 좋은 <b>리뷰</b>를... </description>
            <bloggername>건짱의 Best Drawing World2</bloggername>
            <bloggerlink>http://blog.naver.com/yoonbitgaram</bloggerlink>
            <postdate>20161208</postdate>
        </item>
        ...
    </channel>
</rss>
오류 코드 
검색 API 블로그 검색의 주요 오류 코드는 다음과 같습니다.

오류 코드	HTTP 상태 코드	오류 메시지	설명
SE01	400	Incorrect query request (잘못된 쿼리요청입니다.)	API 요청 URL의 프로토콜, 파라미터 등에 오류가 있는지 확인합니다.
SE02	400	Invalid display value (부적절한 display 값입니다.)	display 파라미터의 값이 허용 범위의 값(1~100)인지 확인합니다.
SE03	400	Invalid start value (부적절한 start 값입니다.)	start 파라미터의 값이 허용 범위의 값(1~1000)인지 확인합니다.
SE04	400	Invalid sort value (부적절한 sort 값입니다.)	sort 파라미터의 값에 오타가 있는지 확인합니다.
SE06	400	Malformed encoding (잘못된 형식의 인코딩입니다.)	검색어를 UTF-8로 인코딩합니다.
SE05	404	Invalid search api (존재하지 않는 검색 api 입니다.)	API 요청 URL에 오타가 있는지 확인합니다.
SE99	500	System Error (시스템 에러)	서버 내부에 오류가 발생했습니다. "개발자 포럼"에 오류를 신고해 주십시오.
403 오류
개발자 센터에 등록한 애플리케이션에서 검색 API를 사용하도록 설정하지 않았다면 'API 권한 없음'을 의미하는 403 오류가 발생할 수 있습니다. 403 오류가 발생했다면 네이버 개발자 센터의 Application > 내 애플리케이션 메뉴에서 오류가 발생한 애플리케이션의 API 설정 탭을 클릭한 다음 검색이 선택돼 있는지 확인해 보십시오.

참고
네이버 오픈API 공통 오류 코드는 "API 공통 가이드"의 '오류 코드'를 참고하십시오.



## 파이썬 구현 예시

```python
# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
```

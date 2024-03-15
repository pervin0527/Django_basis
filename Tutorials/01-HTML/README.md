# What is HTML?

## 1.HyperText Markup Language

- [Hypertext](https://ko.wikipedia.org/wiki/%ED%95%98%EC%9D%B4%ED%8D%BC%ED%85%8D%EC%8A%A4%ED%8A%B8) : 링크(하이퍼링크)를 통해 다른 문서로 이동할 수 있게 하는 텍스트.
- [Markup Language](https://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EC%97%85_%EC%96%B8%EC%96%B4) : 태그(tag)를 이용해 문서나 데이터의 구조를 명기하는 언어.
- 기본적으로 웹페이지에서 보여줄 내용을 담고 있는 "문서"로 프로그래밍이 아니라 "문서를 작성하는 것"이다.
- 브라우저가 HTML 문서를 읽으며 `<h1>`, `<a>` 와 같은 태그를 보면서 해당 라인은 제목 또는 링크임을 파악하고, 이를 유저에게 적절히 보여주는 렌더링(Rendering)작업을 수행함.

        <h1>This is Head1</h1>
        <h2>This is Head2</h2>

## 2.How To Write HTML document?

`doc`를 통해 일반적인 HTML 문서(Typical HTML Document)를 만들어준다. 필수적인 내용들이니 반드시 `doc`를 통해 작성해야한다.

        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>

        </body>
        </html>

`<head>`와 `<body>`를 볼 수 있는데,

- `<head>`는 링크 및 메타데이터 정보들을 포함.

  - `<html lang="en">` 이 문서는 영문으로 작성되어 있음을 명시. 브라우저가 어떤 언어로 작성된 문서인지 인식하게 만든다.
  - `<title>Document</title>` 문서의 제목.

- `<body>`는 문서의 주요 내용, 컨텐츠를 포함.

## 3. `<div>` & `<span>`

`<div>`와 `<span>`은 명확히 구분할 필요가 있다.

- `<div>`는 "division"을 의미, 웹 페이지 내에서 논리적으로 구분된 콘텐츠 영역을 만들기 위해 사용된다. 주로 다양한 콘텐츠와 HTML 요소들을 그룹화하는 데 사용함.
- 핵심적으로 블록 레벨 원소에 해당하며 새로운 줄에서 시작하고 가능한 한 많은 너비를 차지하여 부모 원소의 전체 너비를 채우려한다.

-`<span>`은 인라인 콘텐츠를 위한 컨테이너로, 텍스트나 이미지 같은 콘텐츠에 스타일을 적용하거나, 문서의 일부분에 특정 스타일을 적용하기 위해 사용된다.

- `<span>`은 구조적 의미를 추가하지 않으며 오로지 스타일이나 언어 설정 같은 목적으로 사용한다.

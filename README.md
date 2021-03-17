## Flask_board_project
#### try to make flask board web pages
##
**flask run 명령은 프로젝트 루트 디렉토리에서 실행해야한다.**
> 다른곳에서도 실행되지만 참조경로가 틀어짐

**flask db init**
> 데이터베이스를 관리하는 초기 파일들을 migrations라는 디렉터리에 자동으로 생성해준다.
이때 생성되는 파일들은 Flask-Migrate 라이브러리에서 사용된다. 최초 한번만 수행하면 됨
  
**flask db migrate**
> 모델을 새로 생성하거나 변경할 때 사용

**flask db upgrade**
> 모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용

**플라스크는 데이터 타입이 db.Integer이고 기본키로 지정한 속성은 값이 자동으로 증가하는 특징
 데이터를 저장할 때 해당 속성값을 지정하지 않아도 1씩 자동으로 증가하여 저장된다.**
 ##
 
**필드의 기본값은 설정 방법(db.Column함수)**
> server_default : flask db upgrade 명령을 수행할 때 필드를 갖고 있지 않던 기존 데이터에도 기본값이 저장된다. 

> default는 새로 생성되는 데이터에만 기본값을 생성해 준다. 
#
#
#
#
>> Jump to Flask
>> 
>> https://wikidocs.net/book/4542

import datetime
from pytz import timezone
LOCATION = 'Asia/Shanghai' # 'Asia/Seoul'
SHORT_LOCATION = 'CST'

def get_url(file_name: str) -> str :
    return f"https://github.com/THU-WingTecher/Vulnerabilities/res/{file_name}"

class Writer() :
    def __init__(self) -> None:
        self.path = "Readme.md"
        pass
    
    def dump(self) -> None :
        contents = self.write() 
        with open(self.path, "w") as file :
            file.write(contents)
    
    def load(self) -> str :
        with open(self.path, "r") as file :
            return file.read()

    def get_date() :
        # Get the current date
        current_date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        if current_date.hour+9 >= 24:
            timezone_time = current_date.hour+9-24
        else :
            timezone_time = current_date.hour+9

        currdate = current_date.replace(hour=timezone_time)
        currdate = currdate.replace(second=0)
        currdate=currdate.replace(tzinfo=timezone(LOCATION))
        return f'Last updated : {currdate.strftime("%A, %d %b, %H:%M")} {SHORT_LOCATION}'
    
    def introduce(self) -> str :
        return f"[Provide a brief introduction about your team's bug-finding abilities and goals.]"
    
    def addintional_info(self) -> str :
        return f"[Additional information or conclusion about the projects tested and the impact of your bug-finding capabilities.]"
    def write(self) -> str :
        #FIXME How to validate the file name is right?
        return f"""
## Introduction
{self.introduce()}

## Total Bugs Found
![Total Bugs Found]({get_url('overall.png')})

For detailed information on the bugs we've identified, visit the following links:
- [CVE Details]({get_url('CVE.md')})
- [CNVD Details]({get_url('CNVD.md')})
- [Other Bugs Details]({get_url('others.md')})

## Total Projects Tested
![Total Projects Tested]({get_url('total_projects_tested.png')})

{self.addintional_info()}

"""
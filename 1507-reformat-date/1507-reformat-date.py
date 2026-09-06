class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        year = ""
        month = ""
        day = ""

        if len(date) == 12:
            year = date[8:]
            month = months[date[4:7]]
            day = "0" + date[0]
        if len(date) == 13:
            year = date[9:]
            month = months[date[5:8]]
            day = date[:2]
        
        return year + "-" + month + "-" + day


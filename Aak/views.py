from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index2.html')
def analyze(request):
    if request.method=='POST':
        text=request.POST.get('text')
   # remove punctuations checkbox value getting   
        repunc=request.POST.get('removepunc','default')
        Cap_text=request.POST.get('Text_capital','off')
        Lower_text=request.POST.get('Lower_text','off')
        R_newline=request.POST.get('R_newline','off')
        Char_count=request.POST.get('char_count','off')
        if repunc=='on' :
            analyzed_text=""
            for char in  text:
                if char not in [ '.','?', '!', ',',';',':','—' ,'-' ,'(',')','[',']','{' ,'}' ,'"'  ,"'","'"]:
                    analyzed_text=analyzed_text+char
                
            parmas={'purpose':'Removed Punchuation','analyzed_text':analyzed_text}
        
            text=analyzed_text
        if Cap_text=='on':
            analyzed_text=""
            for char in text:
                analyzed_text=analyzed_text+char.upper()
                
            parmas={'purpose':'Chanaged to uppercase','analyzed_text':analyzed_text}
            text=analyzed_text
        if Lower_text=='on':
            analyzed_text=""
            for char in text:
                analyzed_text=analyzed_text+char.lower()
            parmas={'purpose':'Chanaged to lowercase','analyzed_text':analyzed_text}
            text=analyzed_text 
        if R_newline=="on":
            analyzed_text=""
            for i in text:
                if i!="\n"and i!="\r":
                    analyzed_text=analyzed_text+i
            parmas={'purpose':'Removed Newline character','analyzed_text':analyzed_text}
            text=analyzed_text
        if Char_count=="on":
            i=0
            for char in text:
                i+=1
            parmas={'purpose':f'Total character is {i}','analyzed_text':text}

       
        if (Cap_text!='on'and Char_count!="on"and repunc!='on' and R_newline!="on" and Lower_text!='on'):
            parmas={'purpose':f'do nothing','analyzed_text':text}
    return render(request,'Anlyz.html',parmas)
                

    

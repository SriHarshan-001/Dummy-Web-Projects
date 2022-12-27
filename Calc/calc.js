var eval_string;
var final_expr="";
const num=[];
var result;

function sendNum(digit){
    num.push(digit);
    if(num[0]=="+"||num[0]=="-"||num[0]=="*"||num[0]=="/"||num[0]=="*0.01"){
        document.getElementById("result").innerHTML="Enter a valid expression!";
    }
    if(num.length != 1){
		eval_string = '';
		document.getElementById('screen').innerHTML = eval_string;		
	}

    for(i=0; i<num.length ; i++){

		eval_string = eval_string + num[i];				
		
	}

document.getElementById("result").innerHTML = eval_string;
}

function clrscr(){
    document.getElementById("result").innerHTML="";
    while(num.length>0){
        num.pop();
    }
    eval_string="";
    final_expr="";
}

function equalTo(){
    document.getElementById("result").innerHTML="";
    for(let opr of num){
        final_expr+=opr;
    }
    result=eval(final_expr);
    document.getElementById("result").innerHTML=result;
    while(num.length>0){
        num.pop();
    }
    num.push(result.toString());
}
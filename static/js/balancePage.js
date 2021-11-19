    text ="";
    var images=[];
    var sImages = [];
    var cnt = 0;
    var num =0;
    var sNum = 0;
    var cnt2 =0;
    var select = [];
    document.getElementById('submitButton').style.display='none';
    function show(){
        
        for(i=0; i<8 ;i++){
            images[i] = (i+1)+".PNG";
        }
        images.sort(function(a,b){return 0.5-Math.random()});
        showImg(num);
    }

    

    function showImg(num){
        document.getElementById('submitButton').style.display='none';
        document.getElementById('balanceImg').style.backgroundImage=`url("../static/images/${num+1}.PNG")`;
        document.getElementById('balanceImgs').style.backgroundImage=`url("../static/images/${num+2}.PNG")`;
        cnt2++;
    }

    function change(n){
        if(cnt2<3){
            cnt++;
            if(n==0)
                sImages[sNum++] = images[num];
            else
                sImages[sNum++] = images[num+1];
            num+=2;
            
            showImg(num);
        }
        else{
            document.getElementById('submitButton').style.display='block';
        }
    }

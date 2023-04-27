$(document).ready(function(){

    // red background for all the week-ends in the first loaded page
    if (($('.first_week p:nth-child(6)').text()).length==1){
        $('.first_week p:nth-child(6)').css('background-color','    background-color: #90292bd2;')
    }
    if (($('.first_week p:nth-child(7)').text()).length==1){
        $('.first_week p:nth-child(7)').css('background-color','    background-color: #90292bd2;')
    }
    $('.rest_weeks').each(function() {
        $(this).find('p').eq(6).add($(this).find('p').eq(5)).css('background-color', '#90292bd2');
      });
      
    // calendar class ===================================================


    // click to get the next year
    $('.calendar_icon_y_l').click(function(){
        $('.year_selected').data('value',(parseInt($('.year_selected').data('value'))-1))
        $('.year_selected').text($('.year_selected').data('value'))
    }),

    // click to get he prev year
    $('.calendar_icon_y_r').click(function(){
        $('.year_selected').data('value',(parseInt($('.year_selected').data('value'))+1))
        $('.year_selected').text($('.year_selected').data('value'))
    })


var months=['','janvier' , 'fevrier' , 'mars' , 'avril' , 'mai' , 'juin' , 'juillet' , 'aout' , 'septembre' ,'octobre' , 'novembre' , 'decembre']

    // click to get the next month if the month is december switch to the next year with month equal to "janvier"
    $('.calendar_icon_m_r').click(function(){
        var monthh=$('.month_selected').data('value');
        var index_oldmonth=parseInt(monthh)

        if (index_oldmonth === 12){
            var index_newmonth=1
            var newmonth= months[index_newmonth]
            $('.year_selected').text(parseInt($('.year_selected').text())+1)
            $('.year_selected').data('value' , parseInt($('.year_selected').text()))
        } else {
            var index_newmonth=index_oldmonth+1
            var newmonth= months[index_newmonth]
        }
        
        $('.month_selected').text(newmonth)
        $('.month_selected').data('value' , index_newmonth);

    })

    // click to get the prev month if the month is janvier switsh to the prev year with month equal to "decembre"
    $('.calendar_icon_m_l').click(function(){
        var monthh=$('.month_selected').data('value');
        var index_oldmonth=parseInt(monthh)

        if (index_oldmonth === 1){
            var index_newmonth=12
            var newmonth= months[index_newmonth]
            $('.year_selected').text(parseInt($('.year_selected').text())-1)
            $('.year_selected').data('value' , parseInt($('.year_selected').text()))
        } else {
            var index_newmonth=index_oldmonth-1
            var newmonth= months[index_newmonth]
        }
        
        $('.month_selected').text(newmonth)
        $('.month_selected').data('value' , index_newmonth);
        
    })

    // to load the days of the month in the selected year
    $('.calendar_header img').click(function(){
        var month=parseInt($('.month_selected').data('value'));
        var year = $('.year_selected').text()
        var first_week='';
        $.ajax({
            type : "GET",
            url  : '/calendar_refresh',
            data :{
                'month':month,
                'year':year,
            },
            success : function(response){
                //  coloring the backgroud for each week-end day in the first week 
                for(let i=1 ; i<8 ; i++){
                    if (i<=response.b_days){
                        first_week+="<p class='no_date' style='background: linear-gradient(45deg, #cccccc 50%, transparent 10%, transparent 75%, #cccccc 50%); padding-top: 35px;' ></p>"
                    } else {
                        d=i-response.b_days
                        if(i===6 || i===7){
                            first_week+="<p style='background-color: #90292bd2;' >"+ d +"</p><br>"
                        } else {
                            first_week+="<p>"+ d +"</p><br>"
                        }
                    }
                };
                $('.first_week').html(first_week)
                //  coloring the backgroud for each week-end day in the rest weeks
                // this if statement if the month have 5 or 6 weeks 
                if (response.nbr_weeks == 4){
                    $('.rest_weeks').eq(4).css('visibility',' hidden')
                } else {
                    $('.rest_weeks').eq(4).css('visibility' , 'visible')
                }
                for (let i=0;i<response.nbr_weeks ; i++){
                    var first_day=response.fdir;
                    var last_day=response.last_day
                    var rest_weeks='';
                    y=$('.year_selected').data('value').toString()
                    m=$('.month_selected').data('value').toString()
                    for(let j=first_day+(i*7);j<first_day+(7*(i+1));j++){
                        if(j-1>=last_day){
                            rest_weeks+="<p class='no_date' style='background: linear-gradient(45deg, #cccccc 50%, transparent 10%, transparent 75%, #cccccc 50%); padding-top: 35px;' ></p>"
                        } else {
                            var daye= y+'-'+m+'-'+j.toString()
                            var d= new Date(daye)
                            if (d.getDay()===6 || d.getDay()===0){ 
                                rest_weeks+="<p style='background-color:#90292bd2;' >"+j+'</p><br>'
                            } else {
                                rest_weeks+="<p>"+j+'</p><br>'
                            }
                        }
                    }
                    $('.rest_weeks').eq(i).html(rest_weeks)
                }
            }
        });
    })
// action form class ========================================================

function create_date(date_input, element) {// this function i used to generate the correct date form for the "date" python library
    if ($(element).text().length === 1) {
        var day =$('.year_selected').data('value')+ '-' +  $('.month_selected').data('value') + '-' + '0'+$(element).text();
    } else {
      var day =$('.year_selected').data('value')+ '-' +  $('.month_selected').data('value') + '-' + $(element).text();
    }
    $(date_input).val(day);
  }
  $(document).on('click', '.calendar p:not(.no_date)', function() { // no_date i should change it no_day to be more clear 

    if ($('#start').val() == '') {
      $(this).css('background-color' , 'rgb(133, 177, 133)')
      create_date('#start', this);
      $('#start').css('border-color' , ' #44FCC7')
    } else if ($('#end').val() == '') {
        if ($(this).css('background-color')==="rgb(133, 177, 133)"){
            $('#start').val('')
            $(this).css("background" , 'none')
        } else {
            create_date('#end', this);
            $(this).css('background-color' , 'rgb(133, 177, 133)')
            $('#end').css('border-color' , ' #44FCC7')

        }
    } else if($('#end').val()!='' && $(this).css('background-color')==="rgb(133, 177, 133)" ){
        $('#end').val('')
        $(this).css("background" , 'none')
    }

  });

        // to work on this function (if user select two dates i should automated who the first and secend)
  $(document).on('click', '.submit_date', function(){
    if( new  Date($('#start').val())>new Date($('#end').val())){ // if who select the first date after the seconde date
        $('.message').text('verifier votre dates')
        $('#start').val('')
        $('#end').val('')
        $('p[style*="background-color: rgb(133, 177, 133)').css('background' , 'transparent')
        $('.message').text('wrong dates ')  
    } else if($('.occasion').val().length<3) {
        $('.message').text('remplir le titre d\'occasion correctement ')
    } else {
        var start = $('#start').val().split('-');
        console.log(start)
        var end = $('#end').val().split('-');
        var date_start = new Date(Date.UTC(start[0], start[1] - 1, start[2])); //  start[1]-1 in the case of month beacause Date.utc take the first month (jan) indexed with 0
        var date_end = new Date(Date.UTC(end[0], end[1] - 1, end[2]));
        let current = new Date(date_start);
        var weekends_list = [];
        while (current <= date_end){ // this while to count the number of weekends between the two dates 
        if (current.getUTCDay() === 6 || current.getUTCDay() === 0){
            weekends_list.push(current.toISOString().substring(0, 10));
        }
        current.setUTCDate(current.getUTCDate() + 1); 
        }

        $.ajax({
            type: 'POST',
            url : '/get_days/',
            data :{
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val() ,
                'start_date':$('#start').val(),
                'end_date':$('#end').val(),
                'weekends_list':JSON.stringify(weekends_list),
                'occasion' : $('.occasion').val()
            },
            success : function(response){
                $('#start').val('')
                $('#end').val('')
                $('.occasion').val('')
                $('p[style*="background-color: rgb(133, 177, 133)').css('background' , 'transparent')
                $('.message').text("date saved successfully !")
            }    
        })
    }   
  })


})
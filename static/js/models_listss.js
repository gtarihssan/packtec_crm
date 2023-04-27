$(document).ready(function(){
    $('.add_button').click(function(){
        console.log('success')
        var link=$(this).data('href')
        console.log(link)
        window.location.href = link;
    })

    $('.update_button').click(function(){
        var cheched_inputs = $('input[name=models_ids]:checked').length;
        if (cheched_inputs > 1){
            $('input[name=models_ids]:checked').prop('checked' , false)
            // add message that the user can edit just one model
        } else if (cheched_inputs===1){
            console.log('success')
            var link=$('.update_button').data('href')
            var model_id=$('input[name=models_ids]:checked').val()
            window.location.href = link+model_id
        }
    })
})

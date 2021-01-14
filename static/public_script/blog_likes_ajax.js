(function($){
    $('.like-form').submit(function(e){
        e.preventDefault();

        const blog_id = $(this).attr('id')
        
        const likeText = $(`#like-btn${blog_id}`).text()
        const likeTextTrim = $.trim(likeText)

        const likeCount = $(`#like-count${blog_id}`).text()
        const likeCountInt = parseInt(likeCount)
        
        const url = $(this).attr('action')
        var csrfToken = $("input[name=csrfmiddlewaretoken]").val()
        let result;

        $.ajax({
            url: url,
            data: {
                "csrfmiddlewaretoken": csrfToken,
                "blog_id": blog_id
            },
            type: "post",
            dataType: "json",
            success: function(response){
                if (likeTextTrim === "Unlike"){
                    $(`#like-btn${blog_id}`).text('Like').css({'color':"white", "background-color": "blue"})
                    result = likeCountInt - 1;
                }else{
                    $(`#like-btn${blog_id}`).text('Unlike').css({'color':"white", "background-color": "red"})
                    result = likeCountInt + 1;
                }
                $(`#like-count${blog_id}`).text(result)
            },
            error: function(response){
                console.log("error", response)
            }
        })
    })

})(jQuery);
// alert("regis.js")
// $(jQuery) -> wait for DOM loaded
function bindEmailCaptchaClick(){
  $("#captcha-btn").click(function (event){
    // prevent default event
    event.preventDefault();
    // use self to bind with #captcha-btn
    let self = $(this)

    let email = $("input[name='email']").val();
    $.ajax({
      url: "/auth/verify/email?email="+email,
      method: "GET",
      success: function (result){
        let code = result['code'];
        if(code === 200){
          let countdown = 60;
          self.off("click");
          let timer = setInterval(function () {
            self.text(countdown);
            countdown -= 1;
            // countdown over
            if (countdown <= 0) {
              // clear timer
              clearInterval(timer);
              // replace original text
              self.text("Get Verification Code");
              // rebind click event(start over if code failed to send)
              bindEmailCaptchaClick();
            }
          }, 1000);
        }else{
          alert(result['message']);
        }
      },
      error: function (error){
        console.log(error);
      }
    })
  });
}


// execute after DOM is loaded
$(function (){
  bindEmailCaptchaClick();
});
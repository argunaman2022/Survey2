// Disable "Enter" key to prevent submitting the form accidentally
$('html').bind('keypress', function(e) {
    if(e.keyCode === 13 || e.key == 'Enter') {
       return false;
    }
 })
 // Disable mousewheel from changing the input field, make sure to add noscroll class to the input field.
 document.addEventListener("wheel", function(event){
     if(document.activeElement.type === "number" &&
        document.activeElement.classList.contains("noscroll"))
     {
         document.activeElement.blur();
     }
 });
 
 function myfunction(part){
     // this function is called when the participant interacts with the input field
     // It gets for each choice page the choice of the person and sets the value to the corresponding html element
     let difference_choice=document.getElementById('input-field').value // value chosen by the participant on input field
     let gender_choice=document.getElementById('gender').value  // value chosen by the participant on the dropdown menu
     let choice = difference_choice // this is essentially the difference_choice but is positive for men, negative for women.
 
     if(gender_choice == 'men'){choice = choice}
     else if(gender_choice == 'women'){choice = -choice} //
     
     let current_task=js_vars.tasks[js_vars.round_number-1] // this is the current task
 
     if (part == 2){
       document.getElementById('id_'+ current_task).value=choice
     if (current_task=='Ball_bucket_task_SOB'){
         if(gender_choice=="men"){
             document.getElementById("answer-paragraph").innerHTML = 'Your answer: I think, in Part I, the average person\'s answer to this task was: ' + 'men'.bold() +' scored ' + (difference_choice).toString().bold() +  ' more points than'+' women. '.bold()+
             "In other words, the average person guessed that, on average, men scored " +(10+difference_choice/2).toString().bold() + " points and women " + (10-difference_choice/2).toString().bold()  +  " points."
             }
         else{
             document.getElementById("answer-paragraph").innerHTML ='Your answer: I think, in Part I, the average person\'s answer to this task was: ' + 'women'.bold() +' scored ' + (difference_choice).toString().bold() +  ' more than'+' men. '.bold()+
             "In other words, the average person guessed that, on average, men scored " +(10-difference_choice/2).toString().bold() + " points and women " + (10+difference_choice/2).toString().bold()  +  " points."
             }
         } else{
         if(gender_choice=="men"){
             document.getElementById("answer-paragraph").innerHTML = 'Your answer: I think, in Part I, the average person\'s answer to this task was: ' + 'men'.bold() +' correctly answered ' + (difference_choice).toString().bold() +  ' more questions than'+' women. '.bold()+
             "In other words, the average person guessed that, on average, men answered " +(10+difference_choice/2).toString().bold() + " questions and women " + (10-difference_choice/2).toString().bold()  +  " questions correctly."
         }
         else{
             document.getElementById("answer-paragraph").innerHTML ='Your answer: I think, in Part I, the average person\'s answer to this task was: ' + 'women'.bold() +' correctly answered ' + (difference_choice).toString().bold() +  ' more questions than'+' men. '.bold()+
             "In other words, the average person guessed that, on average, men answered " +(10-difference_choice/2).toString().bold() + " questions and women " + (10+difference_choice/2).toString().bold()  +  " questions correctly."
             }
         }
 
     } else if (part == 1){
          if (current_task=='Attention_Check_1'){
                 if (difference_choice == "73" && gender_choice == "men"){
                 document.getElementById('id_Attention_Check_1').value= 1}
                 else {
                 document.getElementById('id_Attention_Check_1').value= 0}
         } else if (current_task=='Attention_Check_2'){
                 if (difference_choice == "2023" && gender_choice == "men"){
                 document.getElementById('id_Attention_Check_2').value= 1}
                 else {
                 document.getElementById('id_Attention_Check_2').value= 0}
         } else { 
             document.getElementById('id_'+ current_task).value=choice
         }
         if (current_task=='Ball_bucket_task'){
             if(gender_choice=="men"){
                 document.getElementById("answer-paragraph").innerHTML = 'Your answer: I think, on average, ' + 'men'.bold() +' scored ' + (difference_choice).toString().bold() +  ' more points than'+' women. '.bold()+
                 "In other words, on average, men scored " +(10+difference_choice/2).toString().bold() + " points and women " + (10-difference_choice/2).toString().bold()  +  " points."
                 }
             else{
                 document.getElementById("answer-paragraph").innerHTML ='Your answer: I think, on average, ' + 'women'.bold() +' scored ' + (difference_choice).toString().bold() +  ' more than'+' men. '.bold()+
                 "In other words, on average, men scored " +(10-difference_choice/2).toString().bold() + " points and women " + (10+difference_choice/2).toString().bold()  +  " points."
                 }
             } else if (current_task == 'Attention_Check_1'){
                 if(gender_choice=="men"){
                 document.getElementById("answer-paragraph").innerHTML = 'Your answer: I choose "Men" and ' + difference_choice.bold()
                 }
                 else{
                 document.getElementById("answer-paragraph").innerHTML = 'Your answer: I choose "Women" and ' + difference_choice.bold()
                 }
 
         } else{
             if(gender_choice=="men"){
                 document.getElementById("answer-paragraph").innerHTML = 'Your answer: I think, on average, ' + 'men'.bold() +' correctly answered ' + (difference_choice).toString().bold() +  ' more questions than'+' women. '.bold()+
                 "In other words, on average, men answered " +(10+difference_choice/2).toString().bold() + " questions and women " + (10-difference_choice/2).toString().bold()  +  " questions correctly."
             }
             else{
                 document.getElementById("answer-paragraph").innerHTML ='Your answer: I think, on average, ' + 'women'.bold() +' correctly answered ' + (difference_choice).toString().bold() +  ' more questions than'+' men. '.bold()+
                 "In other words, on average, men answered " +(10-difference_choice/2).toString().bold() + " questions and women " + (10+difference_choice/2).toString().bold()  +  " questions correctly."
                 }
             }
     }
 }
 
 
 function funDropdownInput(part){
     let difference_choice=document.getElementById('input-field').value // value chosen by the participant on the dropdown menu
     let gender_choice=document.getElementById('gender').value  // value chosen by the participant on input field
 
     if (gender_choice!="default" && difference_choice!=null){
     myfunction(part)
     document.getElementById("next-button").style.display="inline"
     }
     else {document.getElementById("next-button").style.display="none"}
 }
 
 function funValueInput(part){
     let difference_choice=document.getElementById('input-field').value // value chosen by the participant on the dropdown menu
     let gender_choice=document.getElementById('gender').value  // value chosen by the participant on input field
 
     if (gender_choice!="default" && difference_choice!=null){
     myfunction(part)
     document.getElementById("next-button").style.display="inline"
     }
     else {document.getElementById("next-button").style.display="none"}
 }
 
 function myFunctionReady(){
     document.getElementById("ready-button").style.display="none" // hide the ready-button
     document.getElementById("input-div").style.display="inline" //show the input-div
 }
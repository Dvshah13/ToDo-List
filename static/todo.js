$(function() {
  updateList();
  $('#form').submit(function(event) {
    event.preventDefault();
    myTasks = $('#form').serialize()
    $.post('/add_task', myTasks, function(myTasks){
      $('#task-list').append('<li id="'+ myTasks.id +'" + class = "completed">' + '<input type="checkbox" id="check" />' + myTasks.description + '</li>');
    });
  })

  function updateList(callback){
      $.get('/tasks', function(myTasks) {
        myTasks.forEach(function(myTasks){
       $('#task-list').append('<li id="'+ myTasks.id +'" + class = "completed">' + '<input type="checkbox" id="check" />' + myTasks.description + '</li>');
   })

      })
  }

  $('#task-list').on('click', '#check', function(){
      
     if($(this).prop('checked')){
       var li_id = $(this).closest('li').attr('id');
       console.log(li_id);
       $.post('/mark_task', {"id" : li_id, "done": "True"}, function(){
         console.log("This is working");
       });
     }
     $('#task-list').empty();
     updateList();
   });

});
    //   else {
    //   $(this).closest('li').css("text-decoration","none")
    //     }

// $.post('/mark_task', )

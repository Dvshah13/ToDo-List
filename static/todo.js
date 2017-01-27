$(function() {
  updateList();
  $('#form').submit(function(event) {
    event.preventDefault();
    task = $('#form').serialize()
    $.post('/add_task', task, function(task){
      $('#task-list').append('<li>' + task.description + '</li>');
    });
  })
  function updateList(callback){
      $.get('/tasks', function(task) {
        task.forEach(function(task){
          $('#task-list').append('<li>' + task.description + '</li>');
        })
      })
  };


$.post('/mark_task', )

});

console.log("I'm the player_script file!")

//initial connection emit to server. Explore with other domain/ports
var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on( 'connect', function() {
  socket.emit( 'my event', {
    data: 'User Connected'
  } )


  var form = $( '#chatForm' ).on( 'submit', function( e ) { //for sending chat messages
    e.preventDefault()
    let user_name = $( 'input.username' ).val()
    let user_input = $( 'input.message' ).val()
    socket.emit( 'my event', {
      user_name : user_name,
      message : user_input
    } )
    $( 'input.message' ).val( '' ).focus()//highlights the message field
  } )


  var form = $( '#coopForm' ).on( 'submit', function( e ) { //to send the cheat value
    // console.log('session data is',session['data'])
    e.preventDefault()
    let player = $( 'input.playerNum' ).val()
    let vote = $( 'input.coopVote' ).val()
    socket.emit( 'my vote', {
      player : player,//this isnt showing up on the controller..now it is???
      vote : vote
    } )
  } )


  var form = $( '#cheatForm' ).on( 'submit', function( e ) { //to send the cheat value
    e.preventDefault()
    let player = $('input.playerNum').val()
    let vote = $( 'input.cheatVote' ).val()
    socket.emit( 'my vote', {
      player : player,//this isnt showing up on the controllerr..now it is???
      vote : vote
    } )
  } )
} )


socket.on( 'my response', function( msg ) {
  if( typeof msg.user_name !== 'undefined' ) {
    $( '#noMSG' ).remove()
    $( 'div.message_holder' ).prepend( '<div><b style="color: #000">'+msg.user_name+'</b> '+msg.message+'</div>' )
  }
})


socket.on( 'my vote response', function( msg ) {//vote response
  if( typeof msg.vote !== 'undefined' ) {
    $( '#noMSG' ).remove()
    $( 'div.message_holder' ).prepend( '<div><b style="color: #000">'+'Player '+msg.data.number+'</b> '+'has voted'+'</div>' )
  }

// // If I want to separate the coin counts from showing on the other players screen, I have to build 2 separate HTML and JS files
  $( '#coinCount' ).replaceWith( '<span id="coinCount">'+msg.data.coins+'</span>' )

  // if( typeof msg.data.coins !== 'undefined' ) {
  //   // $( '#coinCount' ).append( '<div>'+msg.data.coins+'</div>' )
  //   $( '#coinCount' ).replaceWith( '<div>'+msg.data.coins+'</div>' )
  // }
})

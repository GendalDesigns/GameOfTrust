console.log("I'm the game_control_script file!")
var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on( 'connect', function() {
    socket.emit( 'my event', {
    data: 'User Connected'
    } )/*
    var form = $( 'form' ).on( 'submit', function( e ) {
    e.preventDefault()
    let user_name = $( 'input.username' ).val()
    let user_input = $( 'input.message' ).val()
    socket.emit( 'my event', {
        user_name : user_name,
        message : user_input
    } )
    $( 'input.message' ).val( '' ).focus()
    } )*/
} )


socket.on( 'my response', function( msg ) {
    if( typeof msg.user_name !== 'undefined' ) {
    $( '#noMSG' ).remove()
    $( 'div.message_holder' ).prepend( '<div><b style="color: #000">'+msg.user_name+'</b> '+msg.message+'</div>' )
    }
})



socket.on( 'my vote response', function( msg ) {
    $( 'div.pv' ).prepend( '<div><b style="color: #000">'+ 'Player '+msg.data.number+'</b> '+msg.vote+'</div>' )
    if (msg.vote=='cheat'){
        msg.count_data.cheat_count=msg.count.cheat_count+1
        $( '#cheatCount' ).replaceWith( '<span id="cheatCount">'+msg.count.cheat_count+'</span>' )

    }
    if (msg.vote=='cheat'){
        msg.count.cheat_count=msg.count.cheat_count+1
    }
})



// socket.on( 'total vote counts', function( msg ) {
//     if (msg.vote=='cheat'){
//         $( '#cheatCount' ).replaceWith( '<span id="cheatCount">'+msg.data.coins+'</span>' )
//     }
//     $( 'div.pv' ).prepend( '<div><b style="color: #000">'+ 'Player '+msg.data.number+'</b> '+msg.vote+'</div>' )

// })

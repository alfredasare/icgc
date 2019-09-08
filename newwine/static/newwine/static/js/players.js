// JavaScript Document

//Audio Playlist
audioPlayer();
function audioPlayer(){
	var currentSong = 0;
	$('#audioPlayer')[0].src = $('#audioPlaylist li a')[0]; //$('#audioPlayer')[0].src Gets the source of the first #audioPlayer element
	//$('#audioPlayer')[0].play(); //To enable autoplay
	$('#audioPlaylist li a').click(function(e){
		e.preventDefault(); // preventDefault stops the default action of the link
		$('#audioPlayer')[0].src = this; //Sets src to clicked link
		$('#audioPlayer')[0].play(); // Plays automatically
		$('#audioPlaylist li').removeClass("current-song");
		currentSong = $(this).parent().index(); //Gets index of parent
		$(this).parent().addClass("current-song");
	});

	$('#audioPlayer')[0].addEventListener('ended',function(){
		currentSong++;
		if(currentSong == $('#audioPlaylist li a').length)
			currentSong = 0;
		$('#audioPlaylist li').removeClass('current-song');
		$('#audioPlaylist li:eq('+currentSong+')').addClass("current-song");
		$('#audioPlayer')[0].src = $('#audioPlaylist li a')[currentSong].href;
		$("#audioPlayer")[0].play();
	}); //To run after audio is done playing
}


//Audio Playlist END

}
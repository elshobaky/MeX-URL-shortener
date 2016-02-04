/* JS File For MelshoX URL Shortener project
 * By : Mahmoud Elshobaky (Mahmoud.elshobaky@gmail.com)
 */
function init() {
	enableButtons ();
	// init clipboard.js
	copyResultToClipboard();
}


function enableButtons () {

	// Set the onclick action for the Shorten URL button
	btn = document.getElementById("url_to_short");
	btn.onclick=function(){shortURL();};
	// Set action for add-details anchor
	$("#add-details").click(function(){
		$("#url-details").toggleClass('hidden');
	});
	// Set action for short again anchor
	$("#short-again").click(function(){
		$("#result").addClass('hidden');
		$("#short-form").removeClass('hidden');
	});

	//$("#copy-btn").click(copyResultToClipboard());

	// Update the button label now that the button is active
	btn.value="Shorten URL";
}


function shortURL () {
	// Get the requested fields
	var url = document.getElementById("url_field").value;
	var direct = document.getElementById("direct-field").checked;
	var title = document.getElementById("title_field").value;
	var description = document.getElementById("description_field").value;
	var fields = {'url': url,'direct': direct,'title':title,'description':description} ;

	$('#url-input').removeClass('error-field');

	$.ajax({
		type     : 'GET',
		url      : '/url/short',
		data     : fields,
		dataType : 'json',
		encode   : true,
		success  : function(data){
			if (data.error) {
				$('#url-input').addClass('error-field');
			}
			else {
				var rootPath = "http://" + window.location.host + "/";
				$('#short-result').attr('value' , rootPath + data.short);
				$('#short-form').addClass('hidden');
				$('#result').removeClass('hidden');
			}
		}
	});
}

function copyResultToClipboard() {
	'use strict';
	// click events
	document.body.addEventListener('click', copy, true);
	// event handler
	function copy(e) {
	// find target element
	var
		t = e.target,
		c = t.dataset.copytarget,
		inp = (c ? document.querySelector(c) : null);
	// is element selectable?
	if (inp && inp.select) {
		// select text
		inp.select();
		try {
			// copy text
			document.execCommand('copy');
			inp.blur();
			// copied animation
			$("#copy-btn-in").addClass('copied')
			$("#copy-btn-in").html('Copied ▲');
			setTimeout(function() { $("#copy-btn-in").html("Copy");$("#copy-btn-in").removeClass('copied'); }, 1500);
		}
		catch (err) {
			alert('please press Ctrl/Cmd+C to copy');
		}
	}
	}
}

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
	// Set action for multi short anchor
	$("#multi-short").click(multiShort);
	// Set action for single short anchor
	$("#single-short").click(singleShort);

	//$("#copy-btn").click(copyResultToClipboard());

	// Update the button label now that the button is active
	btn.value="Shorten URL";
}


function shortURL () {
	// Get the requested fields
	if (document.getElementById("multi_url_field")) {
		var multi_url = document.getElementById("multi_url_field").value;
		var url = false;
	}
	else {
		var multi_url = false;
		var url = document.getElementById("url_field").value;
	}
	var direct = document.getElementById("direct-field").checked;
	var title = document.getElementById("title_field").value;
	var description = document.getElementById("description_field").value;
	var fields = {'url': url,'multi_url':multi_url,'direct': direct,'title':title,'description':description} ;

	$('#url-input').removeClass('error-field');

	$.ajax({
		type     : 'POST',
		url      : '/url/short',
		data     : fields,
		dataType : 'json',
		encode   : true,
		success  : function(data){
			if (data.error) {
				$('#url-input').addClass('error-field');
			}
			else if (data.multi_short) {
				var res = '';
				var rootPath = "http://" + window.location.host + "/";
				for (u in data.urls) {
					if (data.urls[u][0] === 'error') {
						res += data.urls[u][1];
					}
					else {
						res += rootPath;
						res += data.urls[u][1];
					}
					res += '\n'
				}
				var res_html = '<textarea id="short-result">'+res+'</textarea>';
				$('#short-result').replaceWith(res_html);
				$('#short-form').addClass('hidden');
				$('#result').removeClass('hidden');
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

function multiShort() {
	var multi_input = '<textarea id="multi_url_field" name="multi_url"';
	multi_input += ' placeholder="enter each URL in separate line">';
	multi_input += '</textarea>'
	$("#url_field").replaceWith(multi_input);
}

function singleShort() {
	var single_input = '<input id="url_field" name="url" type="url"';
	single_input += ' placeholder="URL ex: http://example.com">';
	$("#multi_url_field").replaceWith(single_input);
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

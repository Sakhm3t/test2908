
function newInput() {;
	$(".inputs").append('<p><input type="text" class="record" required /></p>');
}

function extractDataFromForm()
{
	const records = $('.record').map((_,el) => el.value).get();
	const key_for_records = $('.key').val();

	const keyed_records = { key: key_for_records, items: records };
	const json = JSON.stringify(keyed_records);

	$('.record').remove();
	$('.key').remove();

	const packed_results = `<p><input type="hidden" class="packed" name="json" id="json" value='${json}' /></p>`;
	$(".inputs").append(packed_results);
}

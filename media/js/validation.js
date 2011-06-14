$(document).ready(function()
{
	$('.val input[type=text], .val textarea').blur(function()
	{
		var element = $(this);
		var elementName = element.attr('id');
		var elementValue = element.val();
		var results = 
		{
			valid: true,
			msg: ''
		};

		element.parent().find('img.errorMsg').remove();
		
		switch(elementName)
		{
			case 'providername':
				if(!isAlpha(elementValue) || elementValue == '')
				{
					results.valid = false;
					element.parent().find('div.goodMsg').remove();
				}
				else
				{
					element.parent().find('div.goodMsg').remove();
					element.parent().append('<div class="goodMsg">Check</div>');
				}
				break;
			case 'profilename':
				if(!isAlpha(elementValue))
				{
					results.valid = false;
					element.parent().find('div.goodMsg').remove();
				}
				else
				{
					element.parent().find('div.goodMsg').remove();
					element.parent().append('<div class="goodMsg">Check</div>');
				}
				break;
			case 'partnername':
				if(!isAlpha(elementValue))
				{
					results.valid = false;
					element.parent().find('div.goodMsg').remove();
				}
				else
				{
					element.parent().find('div.goodMsg').remove();
					element.parent().append('<div class="goodMsg">Check</div>');
				}
				break;
			case 'orgname':
                if(!isAlpha(elementValue))
				{
					results.valid = false;
					element.parent().find('div.goodMsg').remove();
				}
				else
				{
					element.parent().find('div.goodMsg').remove();
					element.parent().append('<div class="goodMsg">Check</div>');
				}
				break;
			case 'first_name':
                if(!isAlpha(elementValue))
				{
					results.valid = false;
					element.parent().find('div.goodMsg').remove();
				}
				else
				{
					element.parent().find('div.goodMsg').remove();
					element.parent().append('<div class="goodMsg">Check</div>');
				}
				break;
			case 'last_name':
                if(!isAlpha(elementValue))
				{
					results.valid = false;
					element.parent().find('div.goodMsg').remove();
				}
				else
				{
					element.parent().find('div.goodMsg').remove();
					element.parent().append('<div class="goodMsg">Check</div>');
				}
				break;
			case 'telephone':     
				if (!((elementValue - 0) == elementValue && (elementValue.length > 0)))
				{
					results.valid = false;
					element.parent().find('div.goodMsg').remove();
				}
				else
				{
					element.parent().find('div.goodMsg').remove();
					element.parent().append('<div class="goodMsg">Check</div>');
				}
				break;
			case 'email':
				if (!validateEmail(elementValue))
				{
					results.valid = false;
					element.parent().find('div.goodMsg').remove();
				}
				else
				{
					element.parent().find('div.goodMsg').remove();
					element.parent().append('<div class="goodMsg">Check</div>');
				}
				break;
			default:
				break;
		}
		if(false === results.valid)
		{
			/*element.parent().append('<img class="errorMsg" src="../media/images/erro.png" alt="Erro"/>');*/
		}
		
	});
	
	//Toggles
	//Providers
	$('#udescription').change(function()
	{
		$('#udescriptiontext').slideToggle("slow,");
	});
	
	$("#udescriptiontext").hide();
	
	//Organization
	$('#address').change(function()
	{
		$('.toggle_container').slideToggle("slow,");
	});
	
	$(".toggle_container").hide();
});

function isAlpha(str)
{
	var re = /[^a-z A-Z]/g
	if (re.test(str) || str == '') return false;
	return true;
}

function validateEmail(str)
{
	var x=str;
	var atpos=x.indexOf("@");
	var dotpos=x.lastIndexOf(".");
	if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length)
		return false;
  return true;
}

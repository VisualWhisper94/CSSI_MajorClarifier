let counter = 1;

function addClass()
{
    let value = document.forms['tester']['newclass'].value;
	document.forms['tester']['newclass'].value = "";

    if(value != "")
    {
        let label = document.createElement('label');
        let input = document.createElement('input');

        input.name = "class" + counter;
        counter += 1;
        input.type = "text";
        label.for = input.name;
        label.innerHTML = value + ": ";

        label.appendChild(input);
		label.appendChild(document.createElement('br'))

        document.forms['tester'].insertBefore(label,document.forms['tester']['submit']);
    }

}

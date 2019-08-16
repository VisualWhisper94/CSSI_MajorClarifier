let counter = 1;

function addClass2()
{
    let value = document.forms['tester']['newelement'].value;
    let gpa = document.forms['tester']['gpa'].value;
	document.forms['tester']['newelement'].value = "";
    document.forms['tester']['gpa'].value = "";
    
    if(value != "" && gpa != "" && !isNaN(gpa) && Number(gpa) >= 0.0 && Number(gpa) <= 4.0)
    {
		let parent = document.createElement('div');
        let _class = document.createElement('input');
        let _gpa = document.createElement('input');
       
        _class.name = "class" + counter;
        _gpa.name = "gpa" + counter;
        _class.type = "text";
        _gpa.type = "text";
        _class.value = value;
        _gpa.value = gpa;
        counter += 1;

        parent.className = "userClass";
		parent.appendChild(_class);
        parent.appendChild(_gpa);
		
        document.querySelector('#classList').appendChild(parent);
    }

}
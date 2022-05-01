// reqs 
//slot machine, 3 reels, 5 possible results, 000 +50 XXX +100
// Xs need to be red, O's should be green, JACKPOT! displayed if X X X
//

// slot values
var value_a = document.getElementById('value_a')
var value_b = document.getElementById('value_b')
var value_c = document.getElementById('value_c')
var value_d = document.getElementById('value_d')
var value_e = document.getElementById('value_e')
var value_f = document.getElementById('value_f')
var value_g = document.getElementById('value_g')
var value_h = document.getElementById('value_h')
var value_i = document.getElementById('value_i')
// Reels - static
var reel1 = ['x', '', 'o', '', 'o'];
var reel2 = ['', 'x', '', 'o', ''];
var reel3 = ['x', '', 'o', '', 'o'];
// set default
var reel1pos = 1;
var reel2pos = 1;
var reel3pos = 1;

function setReels(){
// now set reels -- this should always be how they are set, so make it a function?
	// reel1
	if(reel1pos = 0){ $("#value_a").val(reel1[4]);}
	else $("#value_a").val(reel1[reel1pos-1]);
	$("#value_d").val(reel1[reel1pos]);
	if(reel1pos = 4){ $("#value_a").val(reel1[0]);}	
	else $("#value_g").val(reel1[reel1pos+1]);

	//reel2
	if(reel2pos = 0){ $("#value_a").val(reel2[4]);}
	else $("#value_b").val(reel2[reel2pos-1]);
	$("#value_e").val(reel2[reel2pos]);
	if(reel2pos = 4){ $("#value_a").val(reel2[0]);}	
	else $("#value_h").val(reel2[reel2pos+1]);
	
	//reel3
	if(reel3pos = 0){ $("#value_a").val(reel3[4]);}
	else $("#value_c").val(reel3[reel3pos-1]);
	$("#value_f").val(reel3[reel3pos]);
	if(reel3pos = 4){ $("#value_a").val(reel3[0]);}	
	else $("#value_i").val(reel3[reel3pos+1]);
}

function spinReels(){
	reel1pos = getRandomNumber();
	reel2pos = getRandomNumber();
	reel3pos = getRandomNumber();		
}

function pullLever(){
	spinReels();
	setReels();
}

function getRandomNumber(){ return Math.floor(Math.random() % 5); }

function isEnoughMoney(amount) {
    // if (!Number.isInteger(amount) || amount < 1 || amount > 5000) {
    if (isNaN(amount) || amount < 1 || amount > 5000) {
        alert('You are not deserve to play with such money. Valid nterval: [1...5000].');
        return false;
    }
    return true;
}

function isWon(amount) {
    if (amount > 5000) {
        alert('You win! So Lucky!');
        return false;
    }
    return true;
}

function blinkWinMoney() {
    var formInput = document.getElementById('money');
    $(formInput).fadeOut(500);
    $(formInput).fadeIn(500);
}

////snippets from elsewhere, for reference
// initial function. Waits until animation is finished to start calculate payouts.
function startSlotMachine() {
    result = document.getElementById('money').value;

    if (!isWon(result) || !isEnoughMoney(result))
        return;

    result -= 1;
    for (var i = 0; i < winRow.length; i++) {
        if (winRow[i] !== '-1') {
            document.getElementById(winRow[i]).style.background = 'white';
        }
    }
    clearInterval(blinkInterval);
    spinSlotMachine().done(calculatePayout);
}

function spinSlotMachine() {
    let r = $.Deferred();

    $('img').addClass('blur');
    $('img').addClass('top');

    const table = document.getElementById('slotsCollection');
    const numberOfRows = table.rows.length;

    for(let i = 0; i < numberOfRows; i++) {
        let numberOfCells = table.rows[i].cells.length;

        for(let j = 0; j < numberOfCells; j++) {
            let currentCell = table.rows[i].cells[j].getElementsByTagName('*');
            spinEachTableCell($(currentCell), 140 * (j + 1), i, j);
        }
    }

    // if spinning must last 2 seconds, then this solution is not so bad
    setTimeout(function () {
        r.resolve();
    }, 2500);
    return r;
}

function calculatePayout() {
    const result = isPayouts();
    document.getElementById('points').value = result;
}


//// random bits for later. 
// player object
class Player {
	constructor(currency){
		this.currency = currency;
	}
	deduct(amount){
		this.currency -= amount;
	}
	award(amount){
		this.currency += amount;
	}
	// player history, awards, VIP type information would all be here.
}

class Slot{

}

// Slot Machine
class SlotMachine{


	//spin

	//check result

}



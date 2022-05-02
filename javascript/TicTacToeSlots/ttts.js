// reqs 
//slot machine, 3 reels, 5 possible results, 000 +50 XXX +100
// Xs need to be red, O's should be green, JACKPOT! displayed if X X X
//

// Reels - static
var reel1 = ['X', '&nbsp&nbsp', 'O', '&nbsp&nbsp', 'O'];
var reel2 = ['&nbsp&nbsp', 'X', '&nbsp&nbsp', 'O', '&nbsp&nbsp'];
var reel3 = ['X', '&nbsp&nbsp', 'O', '&nbsp&nbsp', 'O'];
// for fun, the odds: XXX Jackpot = 1/125 = 1/5 * 1/5 *1/5 
// odds continued: OOO = 4/125 = 2/5 * 1/5 * 2/5 

// set default reel position
var reel1pos = 1;
var reel2pos = 1;
var reel3pos = 1;
var reelDelay = 2000; // 2 second delay in resolving reel blur / presenting reel

// global as the player's money - this should be made more secure if this were an actual gambling machine
var playerMoney = 0;
var bet = -2;

// instance a global winLine array; important for the logic: a push/pop array for testing win conditions. 
// this would need to be rewritten for multi-line bets. 
var winLine = [];

var blinker; // blinking timer variable to start/stop-- TODO: blinking the cells is still broken

// the main gaming function - the initial setup is in the html, nothing needed for constructors. 
// later, this would be where you pass in the different bet levels 
// which would determine which bet-lines need to be paid attention to for winnings - a bit beyond the scope of this exercise
function pullLever(){
	// clear any messages:
	clearInterval(blinker);
	$('#playerMessage').html('&nbsp;');
	stopBlinking();

	// test to see if there is inserted money, and if the player hasn't beaten a random win condition
    if (!isEnoughMoney(playerMoney)){
    	$('#playerMessage').html('-- Please "insert coins" ');
        return;
    }
    if(!isWon(playerMoney)){
    	return;
    }

	// subtract player money
	cashHandler(bet);
	// choose random reel position
	spinReels();
	// set the reels according to those positions
	setReels();
	// determine if it's a winner, which also will award the money
	determineWinner(); 
	//reset WinLine, which is referenced in setReels
	winLine = [];
}

// sets the reel values. theoretically could be done by a start-spin-then-timer kinda thing
// also where we are going to spin the reels using the animation
function spinReels(){
	reel1pos = getRandomNumber();
	reel2pos = getRandomNumber();
	reel3pos = getRandomNumber();
	//console.log(`Reel positions: ${reel1pos} ${reel2pos} ${reel3pos}`);		
//	blurReels("reel1");
//	blurReels("reel2");
//	blurReels("reel3");
}

function blurReels(reel){
	$(reel).addClass('blur');
    $(reel).addClass('top');
}
function stopBlur(reel){
	$(reel).removeClass('blur');
    $(reel).removeClass('top');	
}

function setReels(){
	// now set reels - this will include stopping the animation after a short interval for each reel
	// rather than dynamically build variables, I'm just passing the info direct for now
	
	// reel1
//	setTimeout(() => {
//		stopBlur('reel1');
		setReel(1, reel1pos, reel1);
//	}, reelDelay);
	// reel2
//	setTimeout(() => {
//		stopBlur('reel2');	
		setReel(2, reel2pos, reel2);
//	}, reelDelay * 2);
	//reel3
//	setTimeout(() => {
//		stopBlur('reel3');
		setReel(3, reel3pos, reel3);		
//	}, reelDelay * 3);
}


// small array size, so passing the reel so that I don't have to dynamically build variable names
// also designed this way because it's an array of characters being passed. 
function setReel(reelNum, reelPos, reelArray){
	reelTop = "#reel"+reelNum+"pos1";
	reelMiddle = "#reel"+reelNum+"pos2";
	reelBottom = "#reel"+reelNum+"pos3";
	//console.log(`in setReel: reel ${reelNum} and ${reelTop} ${reelMiddle} ${reelBottom}, position ${reelPos} and the symbols should be:`);

	//top
	if(reelPos == 0){ 
		$(reelTop).html(reelArray[4]); 
		colorCell(reelArray[4], reelTop);
		//console.log(` ${reelArray[4]}`);
	}
	else {
		$(reelTop).html(reelArray[reelPos-1]); 
		//console.log(` ${reelArray[reelPos-1]}`);
		colorCell(reelArray[reelPos-1], reelTop);
	}
	
	//middle -- also the winning line - needing to push the value to the winLine array
	$(reelMiddle).html(reelArray[reelPos]);
	//console.log(` ${reelArray[reelPos]}`);
	winLine.push(reelArray[reelPos]);
	//console.log(` pushing ${reelArray[reelPos]}`);
	colorCell(reelArray[reelPos], reelMiddle);

	//bottom
	if(reelPos == 4){ 
		$(reelBottom).html(reelArray[0]); 
		//console.log(` ${reelArray[0]}`);
		colorCell(reelArray[0], reelBottom);
	}	
	else { 
		$(reelBottom).html(reelArray[reelPos+1]); 
		//console.log(` ${reelArray[reelPos+1]}`);
		colorCell(reelArray[reelPos+1], reelBottom);
	}
}

function saveCash(){
	pm = Number($('input[id=money]').val());
	if(isEnoughMoney(pm)){
		playerMoney = pm;
		//console.log(`playerMoney is ${playerMoney}`);
		//	$("input[id=currencyNum]").html(playerMoney);	
		$("#currencyNum").html(playerMoney);
		// hide the Cash Bar - TODO: not hiding. 
		$('#cashInput').hide();
	}
}

// in a production environment, this handling would need to be more secured/obscured imho
function cashHandler(value){
	//console.log(`was ${playerMoney} and seeing cash adjustment ${value}`) ;
	playerMoney += value;
	$("#currencyNum").html(playerMoney);
}

// quick and dirty win determination; could also use reel positions 
// -- noting: if this were multiline or any other betting scheme (like winning based on TTT rules), 
// -- -- this would need to be rebuilt. 
function determineWinner(){
	if(winLine[0] == 'X' && winLine[1] == 'X' && winLine[2] == 'X'){
		//console.log("Winner Winner Chicken Dinner X X X");
		playerMoney += 100;
		$("#currencyNum").html(playerMoney);
		$('#playerMessage').html(' -- JACKPOT!!  +100');
		alert('JACKPOT')
		// TODO: This isn't blinking
		blinker = setInterval(blinkWinMoney(), 1000);		
	}
	if(winLine[0] == 'O' && winLine[1] == 'O' && winLine[2] == 'O'){
		//console.log("Winner with the O O O");
		playerMoney += 50;
		$("#currencyNum").html(playerMoney);
		$('#playerMessage').html(' -- You Win!  +50');
		// TODOL this isn't working correctly, blinks once. 
		blinker = setInterval(blinkWinMoney(), 1000);
	}
}

// totally basic, wouldn't pass Gaming Standards reel logic but works for a basic example
// this is where the RNG call would be, for server deterministic ..
// -- to make this not pseudo-random and certifiabe in a real betting system,
// -- -- there would need to be a much better RNG source, amongst the math rework
function getRandomNumber(){ return Math.floor(Math.random() * 5); }

// colors the characters according to their value, called for each reel cell
function colorCell(value, reelCell){
	// clear the cell, then change. 
	$(reelCell).removeClass();

	if(value == 'X') $(reelCell).addClass('red');
	else if(value == 'O') $(reelCell).addClass('green');
	else  $(reelCell).addClass('nocolor');
}

function cashout(){
	// this is where you'd print the ticket or otherwise save the winnings
	// currently just resets the form in default, when pressed; 
	// which is not how the button really should be used in this instance, but works for this example

	// if this were functioning, and not resetting the whole page, this would be needed to return the cashInput box
	$('#cashInput').show();
}

// a silly function with an arbitrary win condition: $5000. 
// if this were a serious game, this wouldn't exist; but I wanted a ceiling for the example, and to make QA easy
function isWon(amount) {
    if (amount > 5000) {
        alert('You win Tic Tac Toe Slots! So Lucky!');
        return false;
    }
    return true;
}

// it blinks the cell. but...
function blinkWinMoney() {
    var formInput = document.getElementById('row2');
    $(formInput).fadeOut(500);
    $(formInput).fadeIn(500);
}
function stopBlinking(){
	var formInput = document.getElementById('row2');
    $(formInput).fadeIn(500);
}

// debug, to test Jackpot win
function makeItRain(){
	$('#playerMessage').html(' -- MAKING IT RAIN');
	reel1pos = 0;
	reel2pos = 1;
	reel3pos = 0;
	setReels();
	determineWinner();
	winLine = [];
}
// debug, to test regular win 
function testWinning(){
	$('#playerMessage').html(' -- testing O O O');
	reel1pos = 4;
	reel2pos = 3;
	reel3pos = 4;
	setReels();
	determineWinner();
	winLine = [];
}

// function to check if there is imaginary money in the machine. 
function isEnoughMoney(amount) {
    // if (!Number.isInteger(amount) || amount < 1 || amount > 5000) {
    if (isNaN(amount) || amount < 1 || amount > 5000) {
        alert('Needs money - Valid numeric interval: [1...5000].');
        return false;
    }
    return true;
}


//////////////////// other ideas, currently unused ///////////////////////


////snippets from elsewhere and git, for reference
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
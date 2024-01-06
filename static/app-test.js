describe('input form callback function tests', function() {
    afterEach(function(){
        const guessInput = document.getElementById('guess-input');
        guessInput.value = '';
    })

    it('should clear the input box when the user clicks in it', function() {
        const guessInput = document.getElementById('guess-input');
        guessInput.value = 'brita';
        spyOn(guessInput, 'click');
        guessInput.click();
        expect(guessInput.click).toHaveBeenCalled();
        expect(guessInput.value).toEqual('');
    })
    it('should clear the feedback space when the user clicks in it', function() {
        const feedback = document.getElementById('feedback-container');
        const guessInput = document.getElementById('guess-input');
        spyOn(guessInput, 'click');
        guessInput.click();
        expect(guessInput.click).toHaveBeenCalled();
        expect(feedback.innerHTML).toEqual('');
    })
})

describe('submit button callback function tests', function(){
    afterEach(function(){
        const guessInput = document.getElementById('guess-input');
        guessInput.value = '';
    })

    it('should pull the correct value from the input box', function() {
        const guessInput = document.getElementById('guess-input');
        guessInput.value = 'brita';
        const submitButton = document.getElementById('submit-button');
        spyOn(submitButton, 'click');
        submitButton.click();
        expect(submitButton.click).toHaveBeenCalled();
        expect(guess).toEqual('brita');
    })
    it('should clear the feedback space', function(){
        const feedback = document.getElementById('feedback-container');
        const submitButton = document.getElementById('submit-button');
        spyOn(submitButton, 'click');
        submitButton.click();
        expect(feedback.innerHTML).toEqual('');
    })
})

describe('sendGuessToServer tests', function() {
    it('should send an axios request to the server', function() {
        expect()
    })

    it('should receive a results dictionary', function() {
        expect()
    })
})

describe('presentFeedback tests', function() {
    it('should display the right feedback based on the results dictionary', function() {
        expect()
    })
})

describe('checkDuplicate tests', function(){
    it('should return false if a word is new'), function(){
        expect()
    }
    it('should add the word to the entered array if it is new'), function(){
        expect()
    }
    it('should return true if a word has been used before'), function(){
        expect()
    }
})

describe('incrementScore tests', function(){
    it('should return the correct score when a new word is entered'), function(){
        expect()
    }
})

describe('updateScore tests', function(){
    it('should update the score on the screen'), function(){
        expect()
    }
})

describe('sendScoreToServer tests', function(){
    it('should receive a response from the axios post request', function(){
        expect()
    })
})

describe('gameOver tests', function(){
    it('should show the play again button when the game is over', function(){
        expect()
    })
})

describe('updateTimer test', function(){
    it('should decrement timer when called', function(){
        expect()
    })
    it('should call game over if the time is up', function(){
        expect()
    })
})
describe('input form callback function tests', function() {
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

// describe('presentFeedback tests', function() {
//     it('should display the right feedback based on the results dictionary', function() {
//         expect()
//     })
// })
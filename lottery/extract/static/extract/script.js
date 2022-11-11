function countCheckedBoxNum() {
    let sum = 0
    document.querySelectorAll('.checkbox-input').forEach(checkBox => {
        if(checkBox.checked === true) {
            sum += 1
        }
    })
    return sum
}

document.addEventListener('DOMContentLoaded', () => {
    let numberInput = document.querySelector('.number-input')
    let checkBoxes = document.querySelectorAll('.checkbox-input')
    checkBoxes.forEach(checkBox => {
        checkBox.addEventListener('change', () => {
            let max_include = countCheckedBoxNum()
            numberInput.max = max_include
        })
    })
})
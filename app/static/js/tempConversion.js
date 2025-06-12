"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
// list of supported temperature units
const tempUnits = ["fahrenheit", "celsius", "kelvin"];
function populateTempDropdowns() {
    const fromSelect = document.getElementById("from-unit");
    const toSelect = document.getElementById("to-unit");
    tempUnits.forEach((unit) => {
        const option1 = document.createElement("option");
        option1.value = unit;
        option1.textContent = unit;
        fromSelect.appendChild(option1);
        const option2 = document.createElement("option");
        option2.value = unit;
        option2.textContent = unit;
        toSelect.appendChild(option2);
    });
    //default selections
    fromSelect.value = "fahrenheit";
    toSelect.value = "celsius";
}
//handle conversion
function convertTemp() {
    return __awaiter(this, void 0, void 0, function* () {
        const valueInput = document.getElementById("value");
        const fromUnitSelect = document.getElementById("from-unit");
        const toUnitSelect = document.getElementById("to-unit");
        const resultDiv = document.getElementById("result");
        const value = valueInput.value;
        const fromUnit = fromUnitSelect.value;
        const toUnit = toUnitSelect.value;
        //clear previous result
        resultDiv.textContent = "";
        //basic validation
        if (!value) {
            resultDiv.textContent = "Please enter a value.";
            return;
        }
        try {
            const response = yield fetch(`/convert/temperature?val=${encodeURIComponent(value)}&from_unit=${encodeURIComponent(fromUnit)}&to_unit=${encodeURIComponent(toUnit)}`);
            const data = yield response.json();
            if (response.ok) {
                resultDiv.textContent = `Result: ${data.result}`;
            }
            else {
                resultDiv.textContent = `Error: ${data.error}`;
            }
        }
        catch (err) {
            resultDiv.textContent = "Network error. Please try again.";
        }
    });
}
//set up event listeners
window.onload = function () {
    populateTempDropdowns();
    const convertButton = document.getElementById("convert-btn");
    convertButton.addEventListener("click", convertTemp);
};

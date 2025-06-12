// list of supported weight units
const weightUnits: string[] = [
  "milligrams",
  "grams",
  "kilograms",
  "ounces",
  "pounds",
];

function populateWeightDropdowns(): void {
  const fromSelect = document.getElementById("from-unit") as HTMLSelectElement;
  const toSelect = document.getElementById("to-unit") as HTMLSelectElement;
  weightUnits.forEach((unit) => {
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
  fromSelect.value = "ounces";
  toSelect.value = "pounds";
}

//handle conversion
async function convertWeight(): Promise<void> {
  const valueInput = document.getElementById("value") as HTMLInputElement;
  const fromUnitSelect = document.getElementById(
    "from-unit",
  ) as HTMLSelectElement;
  const toUnitSelect = document.getElementById("to-unit") as HTMLSelectElement;
  const resultDiv = document.getElementById("result") as HTMLDivElement;

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
    const response = await fetch(
      `/convert/weight?val=${encodeURIComponent(value)}&from_unit=${encodeURIComponent(fromUnit)}&to_unit=${encodeURIComponent(toUnit)}`,
    );
    const data = await response.json();
    if (response.ok) {
      resultDiv.textContent = `Result: ${data.result}`;
    } else {
      resultDiv.textContent = `Error: ${data.error}`;
    }
  } catch (err) {
    resultDiv.textContent = "Network error. Please try again.";
  }
}

//set up event listeners
window.onload = function () {
  populateWeightDropdowns();
  const convertButton = document.getElementById(
    "convert-btn",
  ) as HTMLButtonElement;

  convertButton.addEventListener("click", convertWeight);
};

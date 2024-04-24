function sliderChange(dimension){  
    val = dimension.value;
    const labels = dimension.parentElement.querySelector(".slider-range-labels").querySelectorAll(".label");
    // get the formfield and set its value to the slider value
    field1_name = 'id_' + 'Compet_measure'
    var field1 = document.getElementById(field1_name);
    field1.value = val;

    // Determine the position of the slider value
    const sliderValue = parseFloat(val);
    const thresholds = [0, 1, 2, 3,4,5,6,7,8,9,10]; // Adjust these thresholds as needed
  
      // Remove the "bold-label" class from all labels
      labels.forEach((label) => label.classList.remove("bold-label"));
  
      // Check which label's threshold the slider value falls under and add the "bold-label" class accordingly
      for (let i = 0; i < thresholds.length; i++) {
          if (sliderValue <= thresholds[i]) {
              labels[i].classList.add("bold-label");
              break;
          }
      }
  }
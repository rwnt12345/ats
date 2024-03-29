// JavaScript function to handle selecting a skill
function selectSkill(event, skill) {
    // Prevent default behavior of the link
    event.preventDefault();
    // Display the selected skill beside the "Select Skills" button
    var selectedSkillContainer = document.getElementById("selected-skill-container");
    selectedSkillContainer.textContent = "Selected Skill: " + skill;
}

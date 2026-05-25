---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]"]
cast: "1 minute"
range: "touch"
targets: "up to 1 gallon of non-magical liquid or up to 5 pounds of food"
duration: "1 hour"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You adjust the delicate levels of bitter ingredients in food and drink to draw out their full restorative and fortifying properties. Choose one of the benefits listed below. Any creature that consumes the targeted drink or food gains that benefit. Up to 10 creatures can partake in the meal, and a creature gets no extra benefit for consuming more than one portion.

- Gain 5 temporary Hit Points.

- Gain resistance 2 to fire.

- Gain a +1 circumstance bonus to saves against disease.

**Heightened (4th)** Your remedy provides two benefits of your choice instead of one. The temporary Hit Points increase to 10, the resistance to fire increases to 3, the bonus against disease increases to +2, and the duration is 2 hours.

**Heightened (7th)** The remedy provides all three benefits. The temporary Hit Points increase to 15, the resistance to fire increases to 5, the bonus against disease increases to +3, and the duration is 8 hours.

> [!danger] Effect: Spell Effect: Thermal Remedy

**Source:** `= this.source` (`= this.source-type`)

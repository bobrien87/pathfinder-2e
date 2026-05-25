---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
traits: ["[[Consecration]]", "[[Fire]]"]
cast: "8 hours"
targets: "The city-state of Pol-Bailax"
duration: "instantaneous"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Drawing on the latent power suffused within Pol-Bailax by its phoenix patron, you and the secondary casters send an ephemeral rush of cleansing energy through the city. Those within the area when the ritual successfully concludes are immediately cured of all detrimental emotion and mental effects; affected creatures cease any current hostilities as though they'd failed a save against calm, though this doesn't control their future actions.
- **Critical Success** The ritual's power lingers within its casters, granting them a +1 status bonus against emotion and mental effects for 1 month.

> [!danger] Effect: Spell Effect: Rite of Cleansing Flame (Critical Success)
- **Success** The ritual succeeds.
- **Failure** The ritual has its intended effect, but alters its casters' forms as they fail to contain the phoenix's power. All casters develop a feature reminiscent of a phoenix, such as feathers, glowing red eyes, or talons, and gain weakness 5 to cold and unholy. This is a curse effect.

> [!danger] Effect: Spell Effect: Rite of Cleansing Flame (Failure)
- **Critical Failure** As failure, but each caster must succeed at a DC 17 [[Fortitude]] save or be permanently [[Drained]] 1 for as long as they have the phoenix features.

**Source:** `= this.source` (`= this.source-type`)

---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Darkness]]", "[[Manipulate]]", "[[Shadow]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Reflex"
duration: "10 minutes"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You envelop the target in a shroud of shadow. The target perceives light as one step lower than it actually is (bright light becomes dim light, for example), affecting their ability to sense creatures and objects accordingly.

The shroud also provides the target a +1 status bonus to saving throws against light effects. This effect is helpful to creatures sensitive to light, and a creature can willingly choose to be subject to the failure effect of the spell.
- **Critical Success** The target is unaffected.
- **Success** The effect lasts for 1 round.
- **Failure** The effect lasts its normal duration.

**Source:** `= this.source` (`= this.source-type`)

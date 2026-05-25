---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Focus]]", "[[Hex]]", "[[Manipulate]]", "[[Witch]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Fortitude"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call on your patron to reprimand a creature that has attempted a Deception or Stealth check against you or an ally within the past month. You must be aware they did so. Whenever the target speaks, toads and serpents fall from their lips. The target attempts a Fortitude saving throw. The spell lasts as long as the target remains sickened by it.
- **Critical Success** A few animals fall from their lips, but they're otherwise unaffected.
- **Success** The target is [[Sickened]] 1.
- **Failure** The target is [[Sickened]] 2 and if they perform an action that has the auditory trait or attempt to Cast a Spell, they must succeed at a DC 5 flat check, or the action is disrupted as they choke on an animal.
- **Critical Failure** As failure, and if the target attempts a Deception or Stealth check, their sickened value increases by 1 (to a maximum of [[Sickened]] 4).

**Source:** `= this.source` (`= this.source-type`)

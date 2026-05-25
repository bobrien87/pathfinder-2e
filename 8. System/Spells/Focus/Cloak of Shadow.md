---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Aura]]", "[[Cleric]]", "[[Darkness]]", "[[Focus]]", "[[Manipulate]]", "[[Shadow]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 willing creature"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You drape the target in a mantle of swirling shadows that make it harder to see. The cloak reduces bright light within a 20-foot emanation to dim light. This is a form of magical darkness and can therefore overcome non-magical light or attempt to counteract magical light.

The target can use [[Concealed]] condition gained from the shadows to [[Hide]], though observant creatures can still follow the moving aura of shadow, making it difficult for the target to become completely [[Undetected]]. The target can use an Interact action to remove the cloak and leave it behind as a decoy, where it remains, reducing light for the rest of the spell's duration. If anyone picks up the cloak after it's been removed by the original target, the cloak evaporates and the spell ends.

**Source:** `= this.source` (`= this.source-type`)

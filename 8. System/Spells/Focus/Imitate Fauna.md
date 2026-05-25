---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Illusion]]", "[[Manipulate]]", "[[Ranger]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 willing animal"
duration: "1 hour"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You use your knowledge of nature to pass the target off as a common animal of the same size, representing a species chosen when the spell is cast. This covers the target's visual appearance, scent, and voice. The target can communicate with other members of the species as though they shared a language but can't speak other languages while the spell persists.

Casting *imitate fauna* counts as setting up a disguise for the purpose of the [[Impersonate]] action. It allows the target to ignore any circumstance penalties they might take for being disguised as dissimilar creatures, and it gives the target a +4 status bonus to Deception checks to prevent other animals from seeing through their disguise. You can Dismiss this spell.

> [!danger] Effect: Spell Effect: Imitate Fauna

**Heightened (5th)** You can target up to six willing animals.

**Source:** `= this.source` (`= this.source-type`)

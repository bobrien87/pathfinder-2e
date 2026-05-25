---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Aura]]", "[[Cleric]]", "[[Focus]]", "[[Manipulate]]", "[[Revelation]]"]
cast: "`pf2:1`"
area: "30-foot emanation"
duration: "1 round"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Divine insight lets you see things as they are, unveiled by attempts to magically cloak the truth. The GM attempts a secret counteract check against each illusion that is at least partially within the area. Instead of counteracting the illusion, you see through it (for instance, if the check succeeds against an [[Illusory Disguise]] spell, you see the creature's true form but *illusory disguise* doesn't end). Each time a new illusion comes into the aura during the duration of the spell, the GM attempts a secret counteract check for that illusion.

**Heightened (7th)** You can allow everyone within range of the emanation to see through illusions you succeed against, not just yourself.

**Source:** `= this.source` (`= this.source-type`)

---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "up to 3 creatures"
defense: "Will"
duration: "1 minute or until discharged"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You understand that holding a secret is in itself a kind of power. Each target must attempt a Will save.
- **Success** The target is unaffected.
- **Failure** A rune symbolizing a secret the target is keeping (at the GM's discretion) appears floating in front of you. If that creature attempts a Strike or spell attack against you while you hold their secret, you can discharge the rune as a reaction to deal 7d6 mental damage to the creature.
- **Critical Failure** As failure, but the target becomes convinced you know their secret and takes 1d6 persistent,mental damage from worry. If the rune with the secret is discharged while the creature is still taking the persistent mental damage, the persistent mental damage immediately ends.

**Heightened (+1)** The mental damage increases by 2d6, and the persistent mental damage on a critical failure increases by 1.

**Source:** `= this.source` (`= this.source-type`)

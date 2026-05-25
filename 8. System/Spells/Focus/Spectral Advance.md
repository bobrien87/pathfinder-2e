---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Champion]]", "[[Concentrate]]", "[[Focus]]", "[[Polymorph]]", "[[Spirit]]"]
cast: "1 or 2"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Taking on a spiritual form, you flash across the battlefield to engage an enemy. You Stride to a space adjacent to an enemy. If you cast the spell using 2 actions, you can Stride twice instead of once. If you have a fly Speed, you can Fly instead of Striding.

If you're mounted, you can have your mount move instead of you. Movement from *spectral advance* doesn't trigger reactions and ignores difficult terrain and greater difficult terrain. During the movement, you (or your mount) have resistance equal to your level to all damage.

> [!danger] Effect: Spell Effect: Spectral Advance

**Source:** `= this.source` (`= this.source-type`)

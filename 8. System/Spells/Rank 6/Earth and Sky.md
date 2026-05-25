---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "20-foot emanation"
defense: "Fortitude"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You erupt into the air with the force of a dragon taking flight, launching nearby creatures into the sky with you. This spell has no effect unless you're on solid ground when you cast it. You fly directly upward, up to 100 feet into the air. When the spell ends, you safely float to the ground, as gentle landing. Every other creature in the area when you Cast this Spell must attempt a Fortitude saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature is launched the same distance into the air as you, then falls.
- **Failure** The creature is launched the same distance into the air as you, then falls and can't [[Arrest its Fall]].
- **Critical Failure** As failure, but the creature takes twice as much damage from falling.

**Source:** `= this.source` (`= this.source-type`)

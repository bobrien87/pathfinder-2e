---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Illusion]]", "[[Manipulate]]", "[[Mental]]", "[[Visual]]"]
cast: "`pf2:3`"
range: "60 feet"
area: "10-foot square"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** (continued) four 10-foot-by-10-foot spaces

You create illusory hazards, such as spinning blades or a puddle of acid, in four 10-foot-by–10-foot spaces within range. The hazards are merely a mental projection, and a creature receives a Will save each time it touches a hazard or is occupying one's space at the start of its turn. Depending on the result, the creature takes 4d6 mental damage and might have difficulty moving through the area. A creature can take this damage only once per turn, even if it moves through several hazards. Choose bludgeoning, slashing, piercing, acid, cold, electricity, fire, or sonic damage when you Cast ephemeral hazards; resistances and weaknesses to those damage types apply if the target thinks they do, as judged by the GM. You can freely choose the appearance and damage type of each hazard as long as its appearance reflects the type of damage it deals (for instance, a hazard that deals piercing damage might take the form of sharpened spikes).
- **Critical Success** The creature is unaffected by the hazards and no longer needs to attempt Will saves against them.
- **Success** The creature realizes the hazards aren't real but still takes half damage from them; on future Will saves against the hazards, the creature continues to use this result unless it rolls a critical success.
- **Failure** The target takes full damage and treats the square as difficult terrain.
- **Critical Failure** The target takes double damage and can't pass through a square containing a hazard.

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)

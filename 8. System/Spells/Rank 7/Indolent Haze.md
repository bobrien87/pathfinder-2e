---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]", "[[Sleep]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "20-foot burst"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The faint scent of poppies and a soothing calm fill the area, urging creatures to lay down and take a rest, to do nothing at all, ever again. Creatures in the area when you Cast the Spell must attempt a Will save. Creatures who end their turn in the area must also attempt the save. You can Dismiss the spell.
- **Critical Success** The creature is unaffected.
- **Success** The creature lies down to rest, becoming [[Prone]]. If they were already prone, they instead drift off to sleep, becoming [[Unconscious]].
- **Failure** As success, except that the creature is so happy lying down that they cannot attempt to Stand or otherwise maneuver themself off of the ground on their next turn, though they can [[Crawl]] (potentially to escape the spell's area).
- **Critical Failure** The creature immediately lies down and drifts off to sleep, becoming prone and unconscious. Any creature in the area who is already unconscious when you Cast the Spell (or whose turn ends in the spell's area while they are unconscious) takes 6d4 spirit damage as their life force is drained away through their dreams. This damage does not automatically wake them.

**Heightened (+1)** The spirit damage increases by 2d4.

**Source:** `= this.source` (`= this.source-type`)

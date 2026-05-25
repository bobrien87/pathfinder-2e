---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Air]]", "[[Animist]]", "[[Aura]]", "[[Focus]]"]
cast: "`pf2:1`"
defense: "Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your apparition envelops you in gusting winds that can speed your steps or buffet your foes. When an enemy in the aura critically fails a Strike against you, they must succeed at a Reflex save or become [[Off Guard]] until the end of your next turn. When you cast or sustain this spell, you can either Step, [[Shove]] a creature in the aura using your spell attack modifier in place of your Athletics modifier, or jump 10 feet in any direction (you must land on solid ground, or else you fall).

**Source:** `= this.source` (`= this.source-type`)

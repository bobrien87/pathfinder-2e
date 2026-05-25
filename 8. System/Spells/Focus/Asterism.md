---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "150 feet"
area: "30-foot line"
defense: "basic Reflex"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** (continued) five 30-foot lines

Lines of burning starlight form a constellation around you. Draw five lines, one at a time; each line must anchor at you or a creature or object already connected to a previous line, and it must end at a creature or object within 30 feet of its anchor (possibly allowing the asterism to extend to its full 150-foot range). A creature that begins its turn in one of these lines or enters one of these lines on its turn takes 4d6 fire damage (basic Reflex save). A creature can take this damage only once per turn, even if it moves through several lines. Targets that are part of the asterism do not take damage from it. If the distance between two targets (or you and a target) ever exceeds 30 feet, the line of starlight between the two breaks, and any lines that now no longer have a direct path back to you also break. You can Dismiss the spell.

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)

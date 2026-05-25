---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
area: "5-foot cube"
defense: "Reflex"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** (continued) cube of dirt 5 feet across or smaller

You remove loose dirt, dust, gravel, sand, and the like (though not solid stone) up to the size of a 5-foot cube. Any Medium or smaller creature standing atop the earth when the spell is cast must attempt a Reflex save or [[Acrobatics]] check.
- **Success** The creature is unaffected and can choose to either descend the pit without damage or move to the nearest available space of its choice.
- **Failure** The creature falls [[Prone]] in the nearest available space of its choice or falls into the pit if it prefers.
- **Critical Failure** The creature falls into the pit excavated by the spell and lands prone, taking falling damage as normal.

**Heightened (+2)** The spell can excavate an additional 5-foot cube of earth. If you excavate all four 5-foot cubes beneath a Large creature, it must attempt a Reflex save or Acrobatics check, as above.

**Source:** `= this.source` (`= this.source-type`)

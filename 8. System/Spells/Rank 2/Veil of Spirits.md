---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Spirit]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "20-foot burst"
defense: "Reflex"
duration: "1 minute"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You draw on the essence of spiritual energy surrounding you to manifest a misty veil. When a creature that isn't immune to spirit damage begins its turn within the area, it must attempt a Reflex save. You can Dismiss the veil.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] until the beginning of its next turn.
- **Failure** The creature is dazzled and gains a weakness to spirit damage equal to half your level until the beginning of its next turn as spiritual energy clings to it. A creature with spiritsense can't use that imprecise sense while it's dazzled in this way.
- **Critical Failure** As failure, but the weakness is equal to your level.

> [!danger] Effect: Spell Effect: Veil of Spirits

**Source:** `= this.source` (`= this.source-type`)

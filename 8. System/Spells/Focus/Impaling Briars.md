---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Druid]]", "[[Focus]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:3`"
area: "100-foot emanation"
defense: "Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The ground within the area transforms into a mass of dangerous briars that assault and impede your foes. When you Cast the Supell and the first time you Sustain it each turn on subsequent rounds, select one of the following effects to occur in the area.

- **Ensnare** The briars clump around your foes, attempting to hold them in place. A foe within the area (or flying at most 20 feet above the area) must attempt a Reflex save. On a failure, it takes a –10-foot circumstance penalty to all Speeds for 1 round, and on a critical failure, it is [[Immobilized]] for 1 round unless it Escapes.

- **Impede** The briars twist and writhe, making the entire area difficult terrain.

- **Wall** A [[Wall of Thorns]] appears in the area, lasting for 1 round. The wall is greater difficult terrain instead of difficult terrain.

In addition, once per round you can direct the briars to impale any target in the area (or flying up to 20 feet above the area) that you can see by using a single action, which has the concentrate and manipulate traits. Make a spell attack roll. On a success, the target takes 10d6 piercing damage and takes a –10-foot circumstance penalty to all Speeds for 1 round; on a critical success, the target is Immobilized for 1 round unless it Escapes.

**Source:** `= this.source` (`= this.source-type`)

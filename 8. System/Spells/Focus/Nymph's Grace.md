---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Aura]]", "[[Emotion]]", "[[Focus]]", "[[Incapacitation]]", "[[Mental]]", "[[Visual]]"]
cast: "`pf2:1`"
area: "10-foot emanation"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your apparition manifests as a mask of unearthly beauty that bewilders your enemies. The first time an enemy enters the aura each round, or if they start their turn within the aura, they must succeed at a Will saving throw or become [[Confused]] for 1 round. While confused by this effect, the creature's confused actions never include harming you.

**Source:** `= this.source` (`= this.source-type`)

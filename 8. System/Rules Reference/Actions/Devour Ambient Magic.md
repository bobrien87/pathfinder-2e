---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:r`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Trigger** A creature Casts a Spell with you as the only target

**Effect** Your ostilli radiates cyan light as its tentacle-like filters attempt to consume the magical effect. You can attempt to counteract the triggering spell with an [[Arcana]] check or [[Nature]] check and a counteract rank equal to half your level.

**Source:** `= this.source` (`= this.source-type`)

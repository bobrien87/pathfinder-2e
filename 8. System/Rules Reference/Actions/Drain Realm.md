---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:0`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your previous action was to Sustain your manifested realm

**Requirements** Your manifested realm has a radius of at least 10 feet

**Effect** You siphon power from your manifested realm to bolster your physical form. Decrease your manifested realm's radius by 10 feet. You regain a number of @Damage[(@actor.level)[healing]]{Hit Points equal to your level} and each of your Strikes made before the end of your turn deal an additional 1d8 damage of your realm's damage type.

**Source:** `= this.source` (`= this.source-type`)

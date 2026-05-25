---
type: action
source-type: "Remaster"
traits: ["[[Bravado]]", "[[Swashbuckler]]"]
cast: "`pf2:r`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** A foe within your reach critically fails a Strike against you

You take advantage of an opening from your enemy's fumbled attack. You either make a melee Strike against the triggering foe or attempt to [[Disarm]] it of the weapon it used for the Strike.

**Source:** `= this.source` (`= this.source-type`)

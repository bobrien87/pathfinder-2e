---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Magical]]"]
cast: "`pf2:r`"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** A creature you have successfully Recalled Knowledge about would damage you

**Requirements** You have a free hand

**Effect** You brandish your charm, channeling and shaping the forces within it to protect you against harm. You gain resistance to all damage equal to 2 + half your level rounded up against the triggering effect.

**Source:** `= this.source` (`= this.source-type`)

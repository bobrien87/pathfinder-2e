---
type: action
source-type: "Remaster"
traits: ["[[Death]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You snap off a fragment of your ikon within your opponent's body, which threatens to burst into numerous barbs. Make a Strike with your ikon. If successful, barbs fill the target, dealing two die of weapon damage the first time the creature uses a move action on each of its turns; the barbs are made out of the same material as your weapon ikon and bypass resistances and such accordingly (for instance, a cold iron spear would create cold iron barbs). The barbs last for 1d4 rounds. If the target dies while the barbs are still in their body, the barbs burst forth in a forest of thorns covering the creature's space, which are greater difficult terrain and deal piercing damage equal to half your level for each square that is moved into.

**Source:** `= this.source` (`= this.source-type`)

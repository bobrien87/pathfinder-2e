---
type: action
source-type: "Remaster"
traits: ["[[Arcane]]", "[[Concentrate]]"]
cast: "`pf2:2`"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** Spend 1 Mythic Point. The spirits of four runelords of wrath (Angothane, Xiren, Thybidos, and Alaznist) swirl around you for 1 minute. While the spirits remain, whenever you hit or critically hit with a Reactive Strike, the target takes an additional 5 spirit damage, or 10 spirit damage if the target of your Reactive Strike is Xanderghul, the Runelord of Pride.

**Source:** `= this.source` (`= this.source-type`)

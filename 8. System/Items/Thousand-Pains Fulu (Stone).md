---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]"]
price: "{'gp': 30}"
usage: "affixed-to-a-creature"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Duration** 1 minute

Created by a chirurgeon who threw away morality in search of endless life, a *thousand-pains fulu* blocks the natural flow of elements in the body. A creature to which the fulu is affixed must attempt a DC 19 [[Fortitude]] save. Failure or critical failure primes the target for persistent damage triggered by a specific condition that must be met within the fulu's duration.

This fulu's yellow parchment feels dusty and stiff. The fulu deals 3d6 bludgeoning as muscles swell to crush joints and bones. On a failure or critical failure, if the target takes electricity damage, it takes 1d6 persistent,bludgeoning as well.

**Source:** `= this.source` (`= this.source-type`)

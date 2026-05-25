---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Concealable]]", "[[Concussive]]", "[[Fatal d10]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made for settling disputes when diplomacy fails, dueling pistols are finely crafted and made to fit easily into a holster or pocket. Noble and wealthy merchants in both Alkenstar and Dongun Hold often own matching pairs of dueling pistols in case they're called upon to address a challenge-though this practice has become increasingly rare in the modern age.

**Source:** `= this.source` (`= this.source-type`)

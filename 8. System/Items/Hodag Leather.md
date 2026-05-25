---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 500}"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Dyed green and white and studded with the natural spines of a hodag, this *+1 [[Deathless]] studded leather armor* is an imposing sight, especially when its wearer is barreling towards you.

**Activate—Hodag Toss** `pf2:2` (concentrate, manipulate)

**Effect** You Stride up to your Speed and make a Strike at the end of your movement. If you succeed at your Strike, attempt an [[Athletics]] check against the creature's Fortitude DC. On a success, the creature is thrown 10 feet in a straight line in the direction of your choice and lands [[Prone]]. If the creature is knocked into a solid object, it takes 1d6 bludgeoning damage before landing prone. You can instead toss the creature straight up into the air. The creature lands in the same square it occupied, and takes 1d6 bludgeoning damage as it lands prone. You can't use this ability again for 1d4 rounds.

**Craft Requirements** The initial raw materials must include the hide of a hodag.

**Source:** `= this.source` (`= this.source-type`)

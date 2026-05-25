---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]", "[[Poison]]", "[[Shove]]"]
price: "{'gp': 6250}"
usage: "held-in-one-hand"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The massive stinger of a black scorpion adds significant weight to this *+2 greater striking [[Fearsome]] mace*. On a critical hit, the target is exposed to black scorpion venom.

**Black Scorpion Venom** (poison)

**Saving Throw** DC 36 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 2d12 poison damage and [[Clumsy]] 2 (1 round)

**Stage 2** 3d12 poison damage, clumsy 2, and [[Slowed]] 1 (1 round)

**Stage 3** 4d12 poison damage, [[Clumsy]] 4, and [[Slowed]] 2 (1 round).

**Craft Requirements** The initial raw materials must include the intact stinger of a black scorpion.

**Source:** `= this.source` (`= this.source-type`)

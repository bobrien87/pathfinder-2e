---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Poison]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

Once you imbibe this bitter elixir, your skin exudes a toxin for 1 hour, affecting any creature that hits you with a jaws Strike or other bite attack. If you are Swallowed Whole by another creature, they are automatically exposed to the poison every round and take a –2 penalty to their saving throw against it.

**Frogskin Tincture Poison** (poison)

**Saving Throw** DC 22 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 2d4 poison damage (1 round)

**Stage 2** 2d6 poison damage and [[Enfeebled]] 2 (1 round)

**Stage 3** 3d6 poison damage, [[Enfeebled]] 3, and [[Sickened]] 1 (1 round)

**Source:** `= this.source` (`= this.source-type`)

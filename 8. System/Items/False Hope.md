---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]", "[[Virulent]]"]
price: "{'gp': 2600}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This poison is an insidious distillation of the venom of the boomslang snake. It acts slowly and cyclically, giving its victim a false sense that the poison has failed to take hold or its effects have ended. The GM makes the target's saving throws in secret during any stage that has no effect.

**Saving Throw** DC 37 [[Fortitude]] save (secret)

**Maximum Duration** 10 rounds

**Stage 1** no effect (1 round)

**Stage 2** 10d8 poison damage (1 round)

**Stage 3** no effect

**Stage 4** 12d8 poison damage (1 round)

**Source:** `= this.source` (`= this.source-type`)

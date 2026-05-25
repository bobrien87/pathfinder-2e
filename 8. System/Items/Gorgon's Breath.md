---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Inhaled]]", "[[Poison]]"]
price: "{'gp': 475}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Gorgon's breath is a fine powder that can easily enter living creatures' bloodstreams through their lungs before binding to mucous membranes and causing any nearby soft tissues to harden.

**Saving Throw** DC 32 [[Fortitude]] save

**Onset** 1 round

**Maximum Duration** 6 rounds

**Stage 1** [[Slowed]] 1 (1 round)

**Stage 2** 4d6 bludgeoning damage and slowed 1 (1 round)

**Stage 3** [[Petrified]] (1 round)

**Stage 4** petrified permanently

**Source:** `= this.source` (`= this.source-type`)

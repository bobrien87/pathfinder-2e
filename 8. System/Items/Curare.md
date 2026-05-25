---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Incapacitation]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 100}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` Interact

Hunters all over Golarion favor curare, a potent paralytic derived from boiled tree bark.

**Saving Throw** DC 25 [[Fortitude]] save

**Maximum Duration** 6 rounds (but see stage 3)

**Stage 1** 2d6 poison damage, [[Clumsy]] 1, and [[Enfeebled]] 1 (1 round)

**Stage 2** 3d6 poison damage, [[Clumsy]] 2, [[Enfeebled]] 2, and [[Slowed]] 1 (1 minute)

**Stage 3** 4d6 poison damage, clumsy 2, enfeebled 2, and slowed 1 (1 round). If the victim fails the saving throw while at stage 3, the poison ends and the victim is [[Paralyzed]] for 2d6 minutes.

**Source:** `= this.source` (`= this.source-type`)

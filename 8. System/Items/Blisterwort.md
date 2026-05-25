---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 280}"
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

This clear, viscous liquid causes lesions and blisters that spread quickly. The victim's pain response increases and flesh breaks easily under physical stress.

**Saving Throw** DC 30 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 4d6 poison damage and weakness 2 to physical and force damage

**Stage 2** 5d6 poison damage and weakness 4 to physical and force damage

**Stage 3** 7d6 poison damage and weakness 6 to physical and force damage

**Source:** `= this.source` (`= this.source-type`)

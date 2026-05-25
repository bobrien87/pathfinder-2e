---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 6000}"
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

Pale fade is a white ointment with a sharp, earthy scent. The poison rapidly desiccates flesh, which then crumbles and forms a cloud of pallid dust. If the victim is [[Concealed]] by this poison, then the dust cloud also conceals other creatures from the victim.

**Saving Throw** DC 42 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 10d6 poison damage and [[Drained]] 1 (1 round)

**Stage 2** 12d6 poison damage, drained 1, and concealed (1 round)

**Stage 3** 15d6 poison damage, drained 1, and concealed (1 round)

**Source:** `= this.source` (`= this.source-type`)

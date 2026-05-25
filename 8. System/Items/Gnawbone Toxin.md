---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]"]
price: "{'gp': 235}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` (manipulate)

Made from the ground bones of ghouls or other cannibalistic creatures processed into a green-gray paste, gnawbone toxin imparts an insatiable desire to consume the flesh of intelligent creatures. If the victim eats at least a mouthful of humanoid flesh, it ignores the enfeebled condition from gnawbone toxin for 1 minute. Victims under the effect of gnawbone toxin regain only half as many Hit Points from healing effects unless they've eaten at least a mouthful of humanoid flesh in the last minute.

**Saving Throw** DC 30 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 minutes

**Stage 1** [[Enfeebled]] 2 (1 minute)

**Stage 2** [[Enfeebled]] 3 (1 minute)

**Stage 3** [[Enfeebled]] 4 (`gmr 1d4` minutes)

**Source:** `= this.source` (`= this.source-type`)

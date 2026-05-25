---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]"]
price: "{'gp': 6}"
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

The poison known as looter's lethargy ensures no thieves are strong enough to walk off with pilfered treasures. Commonly smeared on locks, chests, and even valuable items themselves, the poison slowly saps the strength of those who touch it. Nearby guardians can then simply follow the resulting trail of discarded valuables to find the weakened trespasser.

**Saving Throw** DC 19 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 1 hour

**Stage 1** reduce Bulk limit by 3 (1 minute)

**Stage 2** [[Off Guard]], reduce Bulk limit by 4 (10 minutes)

**Stage 3** off-guard, reduce Bulk limit by 5 (10 minutes)

**Source:** `= this.source` (`= this.source-type`)

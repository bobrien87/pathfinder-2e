---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]", "[[Vitality]]"]
price: "{'gp': 18}"
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

Brewed from a plant native to the First World, brightshade destroys tissue, living or dead. Victims of this poison take poison damage if they're alive and vitality damage if they're undead.

**Saving Throw** DC 21 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 1d6 poison or vitality damage (1 round)

**Stage 2** 2d6 poison or vitality damage (1 round)

**Source:** `= this.source` (`= this.source-type`)

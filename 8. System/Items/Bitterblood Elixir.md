---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 40}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #214: The Broken Palace"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Bitterblood elixir is a pale pink color, like that of water tinted by a few drops of blood. After you drink this elixir, your blood becomes dangerous for other creatures to consume. For the next hour, whenever a creature drinks your blood, the elixir changes your blood into a foul-tasting acid as it mixes with the drinker's saliva. You're unharmed by this transformation, but the blood drinker must attempt a DC 20 [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes 2d6 acid damage and is [[Sickened]] 1.
- **Failure** The creature takes 4d6 acid damage and is [[Sickened]] 2.
- **Critical Failure** The creature takes @Damage[4d6[acid],2d6[persistent,acid]] damage, and is [[Sickened]] 3.

**Source:** `= this.source` (`= this.source-type`)

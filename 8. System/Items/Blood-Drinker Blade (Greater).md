---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Versatile s]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #213: Thirst for Blood"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking wounding shortsword* has the design of a fanged mouth carved into the handle. Whenever the blade draws blood, it glows with a dull red energy, as if empowered by the taste of blood.

**Activate—Drink Life** `pf2:2` (concentration)

**Frequency** once per hour

**Effect** The blood-drinker blade guides your hand to cut a foe and feeds you from their blood. Make a Strike with the blade. On a hit, the attack deals an additional 1d8 persistent bleed damage. You also gain 1d8 temporary Hit Points for 1 minute.

> [!danger] Effect: Blood Drinker Blade

**Activate—Exsanguinate** `pf2:1` (concentrate)

**Frequency** once per day

**Requirements** Your most recent action was to successfully deal persistent bleed damage to a creature with Drink Life

**Effect** The blade's power draws even more blood from your victim. The required creature takes 6d6 bleed damage. You gain temporary Hit Points equal to half the bleed damage the creature takes (after applying resistances and the like). You lose any remaining temporary Hit Points after 1 minute.

**Source:** `= this.source` (`= this.source-type`)

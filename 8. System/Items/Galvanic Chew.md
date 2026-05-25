---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Lozenge]]"]
price: "{'gp': 75}"
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

A galvanic chew is a processed ball of dried electric eel, roasted until chewy and coated in spicy, reagent-infused powder that tingles with electricity as you chew. For up to 1 hour, you have resistance 5 to electricity.

> [!danger] Effect: Galvanic Chew

**Secondary Effect** `pf2:r` (electricity)

**Trigger** You're hit by a melee attack or touched by a creature

**Effect** You channel electricity into the triggering creature, which must succeed at a DC 24 [[Fortitude]] save or be [[Stunned]] 1 (or [[Stunned]] 2 on a critical failure). The chew becomes inert. You're then temporarily immune to galvanic chews for 24 hours or until the next time you make your daily preparations.

**Source:** `= this.source` (`= this.source-type`)

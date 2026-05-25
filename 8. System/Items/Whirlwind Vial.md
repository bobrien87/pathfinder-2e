---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Air]]", "[[Alchemical]]", "[[Consumable]]", "[[Expandable]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Opening this vial releases a mighty gust, forming into a fearsome Huge elemental hurricane. The elemental breathes a @Template[cone|distance:30] of air. Each creature in the cone must succeed at a DC 28 [[Fortitude]] save or be knocked away from the elemental. A creature knocked into a solid object stops moving and takes 4d6 bludgeoning.
- **Critical Success** The creature is unaffected.
- **Success** The creature is pushed 10 feet.
- **Failure** The creature is pushed 20 feet.
- **Critical Failure** The creature is pushed 20 feet and knocked [[Prone]].

**Craft Requirements** Supply magical residue from a slain elemental hurricane.

**Source:** `= this.source` (`= this.source-type`)

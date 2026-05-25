---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]", "[[Modular]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking hand cannon* is crafted by wrapping the water-producing organ cluster of a grodair around its barrel, eliminating the need for ammunition, though the living tissue must be maintained with 1 sp of specialized nutrient feed each day. If not, its misfire check is DC 10 flat check. If you fail this misfire check, the organ bursts, dealing an amount of @Damage[(2*@item.system.damage.dice)[bludgeoning]]{bludgeoning damage} equal to double the number of weapon damage dice to you and rendering the *hydrocannon* broken.

**Activate—Tinker Shot** `pf2:2` (manipulation)

**Frequency** once per minute

**Effect** You fiddle with the pressure regulator on the *hydrocannon* and then make a ranged Strike with the gun. A successful attack has an additional effect depending on which modular configuration the *hydrocannon* is currently in.

- **Bludgeoning** The target is pushed 5 feet away from you; this forced movement is increased to 10 feet on a critical hit.

- **Piercing** The target takes a –10-foot circumstance penalty to its Speeds for 1 round.

- **Slashing** The target takes 1d6 bleed damage.

**Craft Requirements** The initial raw materials must include the extradimensional organ cluster extracted from a grodair. Harvesting the organs of a grodair in this way differs greatly from the normal method; it takes an hour and a successful DC 22 [[Arcana]] check. On a critical failure, the organ cluster bursts and deals 4d6 bludgeoning damage to the harvester.

**Source:** `= this.source` (`= this.source-type`)

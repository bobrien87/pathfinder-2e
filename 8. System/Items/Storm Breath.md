---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Air]]", "[[Bottled breath]]", "[[Consumable]]", "[[Electricity]]", "[[Magical]]"]
price: "{'gp': 125}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Storm breaths* are bottles of temperamental lightning captured during storms on the Plane of Air, releasing small charges of static energy any time they're touched. The first *storm breaths* were created by Ranginori's faithful following the Elemental Lord's return from a long imprisonment, but the recipe has since been duplicated across the multiverse.

After inhaling *storm breath*, you gain resistance 5 to both electricity and sonic. You can exhale the *storm breath* as a bolt of lightning, dealing @Damage[4d12[electricity]|options:area-damage] damage to all creatures in a @Template[line|distance:30], with a DC 25 [[Reflex]] save.

> [!danger] Effect: Storm Breath

**Source:** `= this.source` (`= this.source-type`)

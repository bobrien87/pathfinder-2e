---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Lozenge]]"]
price: "{'gp': 1000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate**`pf2:1` (manipulate)

This tangy gum cracks and pops in your mouth as you chew it. While you're chewing crackling bubble gum, for up to 10 minutes, you have a +3 item bonus to saving throws against auditory and sonic effects.

> [!danger] Effect: Crackling Bubble Gum

**Secondary Effect** `pf2:2` (sonic)

**Effect** You blow a bubble with the gum until it pops, after which it becomes inert. The pop deals 9d4 sonic to all creatures in a @Template[cone|distance:15] with a DC 34 [[Fortitude]] save. A creature that fails its save is also bound with sticky gum, taking a –10-foot item penalty to its Speed for 1 minute. The creature can remove the gum with a total of 3 Interact actions. These actions don't have to be consecutive, and other creatures can provide the actions as well.

> [!danger] Effect: Crackling Bubble Gum (Failure)

**Source:** `= this.source` (`= this.source-type`)

---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Expandable]]"]
price: "{'gp': 100}"
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

Miniature octopus arms press up against the sides of this bottle, obscuring the rest of its contents. When opened, a Huge octopus bursts forth, which can appear in water instead of on the ground. Its arms attempt to grasp a creature with a reach of 15 feet. The octopus repositions that creature to a different space within its reach unless the target succeeds at a DC 24 [[Fortitude]] save.

If the octopus is in water, it then releases a cloud of ink in a @Template[emanation|distance:30]. This cloud has no effect outside of water. Creatures inside the cloud are undetected and can't use their sense of smell. The cloud dissipates after 1 minute.

**Craft Requirements** Supply the corpse of a giant octupus.

**Source:** `= this.source` (`= this.source-type`)

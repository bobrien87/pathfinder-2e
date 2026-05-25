---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 25}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This bright oil, first created by humans as a tool to help them fight in darkness, holds flecks of tiny gemstones in suspension and smells like a struck matchstick.

The first time a weapon coated with this oil damages a creature, the wound glows with light for 1 minute. If the creature is [[Invisible]], the light's position means it's merely [[Hidden]] to creatures that would otherwise be unable to see it, rather than undetected. The light also negates the [[Concealed]] condition due to lighting conditions. If the coated weapon doesn't damage a creature within 1 hour, the oil sloughs off and loses its power.

**Source:** `= this.source` (`= this.source-type`)

---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 140}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

**Access** Tian Xia origin

This robust porridge—made from a cockatrice distilled into a broth, hot peppers from a demonic source, and various toppings—causes diners to utter a ghostly wail from the intense heat.

Consuming the porridge grants you a +2 item bonus to saving throws against being [[Petrified]] for 1 hour. You also gain resistance 3 against physical damage for the duration.

> [!danger] Effect: Ghost Fowl Porridge

**Source:** `= this.source` (`= this.source-type`)

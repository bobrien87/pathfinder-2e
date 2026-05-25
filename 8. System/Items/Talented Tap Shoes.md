---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1250}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These stylish shoes were originally created by the Tappin' Toes Troupe, a group of tap-dancing Taldan bards who achieved massive popularity for their line dance routines. Notoriously lazy when it came to practicing choreography, the troupe enchanted their footwear to enhance their agility. Upon retirement, the troupe sold off their shoe designs, and talented tap shoes have become popular among professional dancers ever since. While wearing the shoes, you gain a +2 item bonus to Acrobatics checks to [[Balance]] and [[Tumble Through]] an enemy's space and to Performance checks using dance.

**Activate—Strut Your Stuff** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You click the toes of your talented tap shoes on the ground, and for the next minute, whenever you succeed or critically succeed at a Reflex save to avoid a damaging effect, you can Stride half your Speed as a reaction. However, during this time, you take a –2 item penalty to Stealth checks to [[Sneak]].

> [!danger] Effect: Talented Tap Shoes

**Source:** `= this.source` (`= this.source-type`)

---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "worncloak"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This thin cloak is surprisingly light, as if clouds or the very wind were woven together to make the garment. The cloak grants you a +3 item bonus to Acrobatics checks. When you invest the cloak, you either increase your Dexterity modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate—Ride the Wind** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You tug on the cloak, wrapping yourself in the power of wind. You gain a fly Speed of 30 feet for 1 hour. While wrapped in the cloak, you become translucent, causing you to become [[Concealed]] for the duration.

> [!danger] Effect: Cloak of Swiftness

**Source:** `= this.source` (`= this.source-type`)

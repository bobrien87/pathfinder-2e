---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 25}"
usage: "worn"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Organizations generally buy these simple squares of fabric in large batches with an invisible symbol on each. They help armies composed of troops unfamiliar with each other, such as mercenaries or conscripts, to recognize allied units. The kerchiefs might be tied around the head, neck, or arm. They can also be used to root out impostors.

**Activate—Identify Allies** `pf2:f` (concentrate)

**Trigger** You move within 15 feet of a creature wearing a matching ally's kerchief

**Effect** The symbol magically glows above your head. It's invisible to everyone not invested in a matching ally's kerchief.

**Source:** `= this.source` (`= this.source-type`)

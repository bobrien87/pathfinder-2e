---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 230}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This sprig of berry-festooned holly and mistletoe doesn't wilt or rot. It can be used as a primal locus, and it grants a +1 item bonus to Nature checks while you wear it.

**Activate—Anoint** `pf2:2` (manipulate)

**Frequency** once per 10 minutes

**Effect** You squeeze juice from one of the berries and smear it onto a weapon made primarily of wood to cast [[Runic Weapon]] on it, or onto a creature to cast [[Runic Body]] on it.

**Activate—Bind** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You touch the sprig, then a tree to cast [[One with Plants]] upon yourself, turning into a vine on the touched tree.

**Source:** `= this.source` (`= this.source-type`)

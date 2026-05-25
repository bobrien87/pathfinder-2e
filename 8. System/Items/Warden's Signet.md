---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Focused]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 1250}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This symbol shows your dedication to the magic practiced by some rangers. Most rangers wear it on an amulet, ring, or piercing. You gain a +2 item bonus to Nature checks.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can use only to cast a ranger warden spell. When you use this Focus Point, the warden's signet also casts a 4th-rank [[Oaken Resilience]] spell on you. If not used by the end of your turn, this Focus Point is lost.

**Craft Requirements** You are a ranger with at least one warden spell.

**Source:** `= this.source` (`= this.source-type`)

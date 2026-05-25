---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 80}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *hunter's arrowhead* is meant to be worn as a charm, such as a pendant, or carried in a pocket or quiver. The arrowhead is etched with images sacred to the elven god Ketephys. While you wear or carry the arrowhead, it infuses you with great skill at hunting, and you gain a +1 item bonus to Survival checks and attack rolls against any creature you've currently designated as your prey with [[Hunt Prey]]. A hunter's arrowhead is also a religious symbol of Ketephys.

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** You would miss with an attack made with a bow

**Effect** You gain a +2 circumstance bonus to your attack roll, possibly turning a miss into a hit.

**Source:** `= this.source` (`= this.source-type`)

---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 100}"
usage: "worn"
bulk: "—"
source: "Pathfinder #214: The Broken Palace"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Anyone can use an *essence forge* to craft an *essence charm* without needing to know the formula for an *essence charm*. No larger than a coin, an *essence charm* is normally worn around the neck or hung from a belt—its exact appearance is up to the crafter. When an *essence charm* is created, its crafter selects a skill in which they are at least trained. The *essence charm* grants a +1 item bonus to that skill when worn.

**Activate—Lucky Charm** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You fail or critically fail a check using the *essence charm*'s chosen skill

**Effect** A failed check becomes a success, and a critical failure becomes a failure.

**Source:** `= this.source` (`= this.source-type`)

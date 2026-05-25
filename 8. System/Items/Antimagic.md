---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]"]
price: "{'gp': 6500}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This intricate rune displaces spell energy, granting you a +1 status bonus to saving throws against magical effects.

**Activate—Antimagic Armor** R (concentrate)

**Frequency** once per day

**Trigger** A spell targets you or includes you in its area

**Effect** The armor attempts to counteract the triggering spell with the effect of a 7th-rank [[Dispel Magic]] spell and a counteract modifier of +26.

**Craft Requirements** Supply one casting of *dispel magic*.

**Source:** `= this.source` (`= this.source-type`)

---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Divine]]", "[[Focused]]", "[[Invested]]"]
price: "{'gp': 1250}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These vestments are made of panels showing various scenes from the legends of a particular deity. It serves as a religious symbol of that deity, and you gain a +2 item bonus to Religion checks. When you cast *harm* or *heal*, healing granted to followers of that deity is increased by the rank of the spell.

**Activate—Domain Devotion** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** Gain 1 Focus Point, which you can spend only to cast a cleric domain spell for a domain belonging to the deity the vestments are dedicated to. If you don't spend this point by the end of this turn, it is lost.

**Craft Requirements** You are a cleric who worships the deity tied to the vestments.

**Source:** `= this.source` (`= this.source-type`)

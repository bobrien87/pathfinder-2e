---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Comfort]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 160}"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This padded armor is favored by trackers and foragers who frequent uninhabited forests and brush lands. The armor enables you to communicate with wildlife and other animals.

**Activate—Commune** `pf2:1` (concentrate, primal)

**Frequency** once per day

**Effect** You cast [[Speak with Animals]] on yourself.

**Craft Requirements** Supply a casting of *speak with animals*.

**Source:** `= this.source` (`= this.source-type`)

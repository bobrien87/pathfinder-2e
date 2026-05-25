---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Healing]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

The elixir of rejuvenation restores a creature to full health and eradicates toxins affecting it. When you drink this elixir, you're restored to your maximum Hit Points, and all afflictions of 20th level or lower affecting you are removed.

You can instead administer this elixir to a creature that has been dead for a week or less. When you do, that creature is instantly brought back to life with 1 Hit Point and no spell slots, Focus Points, or other daily resources.

**Craft Requirements** philosopher's stone, true elixir of life

**Source:** `= this.source` (`= this.source-type`)

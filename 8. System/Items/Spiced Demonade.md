---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 8}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

There are some who claim that the original version of this tart red drink contained the ground skin of actual demons, but in truth, spiced demonade was created by a first-year academy student desperate to look awake and alert after a night of carousing.

After consuming spiced demonade, you ignore all effects and penalties from the consumption of alcohol and lack of sleep for 1 hour. These effects resume when the spiced demonade wears off, and you become temporarily immune to spiced demonade for 24 hours.

**Source:** `= this.source` (`= this.source-type`)

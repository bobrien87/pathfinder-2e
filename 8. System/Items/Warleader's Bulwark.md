---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1000}"
bulk: "2"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 resilient breastplate* is made from shining bronze overlaid with reinforcing golden panels emblazoned with images of loyal soldiers. Wearing this breastplate grants you a commanding aura. You gain a +2 item bonus to Diplomacy checks, but you take a -2 item penalty to Stealth checks to [[Hide]] and [[Sneak]] and Deception checks to [[Impersonate]].

**Activate—Command Bravery** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** You grant allies within 100 feet a +2 status bonus to saves against fear effects for 1 minute. When you activate this ability, each affected ally who's [[Frightened]] reduces their frightened value by 1.

> [!danger] Effect: Command Bravery

**Source:** `= this.source` (`= this.source-type`)

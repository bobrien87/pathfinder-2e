---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This thick, blood-red elixir sharpens your senses and makes you more acutely aware of blood. You gain blood sight as an imprecise sense with a duration of 10 minutes. Blood sight has a range of 60 feet and allows you to detect living creatures who are taking persistent bleed damage or who have the dying or wounded conditions. You also detect free-standing puddles or droplets of recently spilled blood. At the GM's discretion, living creatures without blood can't be detected with your blood sight.

**Source:** `= this.source` (`= this.source-type`)

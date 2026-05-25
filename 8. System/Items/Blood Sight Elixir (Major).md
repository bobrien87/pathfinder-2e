---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 350}"
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

This thick, blood-red elixir sharpens your senses and makes you more acutely aware of blood. You gain blood sight as a precise sense with a duration of 1 hour. Blood sight has a range of 60 feet and allows you to detect living creatures who are taking persistent bleed damage or who have the dying or wounded conditions. You also detect free-standing puddles or droplets of recently spilled blood. At the GM's discretion, living creatures without blood can't be detected with your blood sight.

Your blood sight is especially accurate, allowing you to also detect creatures whose Hit Points are currently at half or less of their maximum. When you detect a creature with blood sight, you get a vague approximation of the value of the creature's bleed damage, dying condition, or wounded condition. This approximation can be noticed as "excessive bleeding," a creature being "near death," or some other general sense that doesn't give the exact value.

**Source:** `= this.source` (`= this.source-type`)

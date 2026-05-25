---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

Upon drinking this potion, your biology instantly transforms to take on a set of sexual characteristics of your choice, changing your appearance and physiology accordingly. You have mild control over the details of this change, but you retain a strong "family resemblance" to your former appearance.

The magic functions instantaneously and can't be counteracted. Your new anatomy is as healthy and functional as your previous body's, potentially allowing you to procreate (depending on your ancestry's biology). Drinking a subsequent *serum of sex shift* allows you to either revert back to your original form or adopt other sexual characteristics, as you choose. The elixir has no effect if you are pregnant or from an ancestry with no sexual differentiation. Most ancestries have a wide spectrum of sexual differentiation, some common, others more rare.

**Source:** `= this.source` (`= this.source-type`)
